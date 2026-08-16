from django.shortcuts import render,redirect
from..forms import AttendenceForm
from django.contrib.auth.decorators import login_required
from ..models import Attendence,Subjects
from django.contrib import messages
from django.core.exceptions import PermissionDenied
@login_required
def add_attend(request):

    if not request.user.has_perm("my_app.add_attendence"):
        raise PermissionDenied

    if request.method == "POST":

        form = AttendenceForm(
            request.POST,
            user=request.user
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Attendance Submitted Successfully"
            )
            return redirect("view_attend")

    else:
        form = AttendenceForm(
            user=request.user
        )

    return render(
        request,
        "attendance/add.html",
        {"form": form}
    )

@login_required
def view_attend(request):

    if not request.user.has_perm("my_app.view_attendence"):
        raise PermissionDenied

    if request.user.groups.filter(name="Teachers").exists():

        teacher = request.user.teachers

        teacher_classes = Subjects.objects.filter(
            teacher=teacher
        ).values_list('school_class_id', flat=True)

        get_atd = Attendence.objects.filter(
            student__school_class_id__in=teacher_classes
        )

    else:
        # Admin and other authorized users
        get_atd = Attendence.objects.all()

    return render(
        request,
        'attendance/list.html',
        {'get_atd': get_atd}
    )

@login_required
def detail_attend(request,id):
    if not request.user.has_perm("my_app.view_attendence"):
        raise PermissionDenied
    get_atd=Attendence.objects.filter(id=id).first
    return render(request,'attendance/detail.html',{'get_atd':get_atd})

@login_required
def update_attend(request,id):
    if not request.user.has_perm("my_app.change_attendence"):
            raise PermissionDenied
    try:
        get_atd=Attendence.objects.get(id=id)

    except Attendence.DoesNotExist:

        return redirect("view_attend")
    if request.method=="POST":
        form=AttendenceForm(request.POST,instance=get_atd)

        if form.is_valid():
            form.save()
            messages.success(request,"Updated SuccessFully")
            return redirect('view_attend')
    else:
        messages.error(request,"invalid data try again")
        form=AttendenceForm(instance=get_atd)
        return render(request,"attendance/add.html",{'form':form})

@login_required
def delete_attend(request,id):
    if not request.user.has_perm("my_app.delete_attend"):
            raise PermissionDenied
    try:
        get_atd=Attendence.objects.get(id=id)
    except Attendence.DoesNotExist:
        return redirect('view_attend')

    if request.method=="POST":
        get_atd.delete()
        messages.success(request,"Deleted SuccessFully")
        return redirect('view_attend')
    
    return render(request,'attendance/delete.html',{'get_atd':get_atd})






    return render(request,'attendances/delete.html')


