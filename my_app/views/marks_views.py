from django.shortcuts import render,redirect
from..forms import MarksForm
from django.contrib.auth.decorators import login_required
from ..models import Marks,Subjects
from django.contrib import messages
from django.core.exceptions import PermissionDenied

@login_required
def add_marks(request):

    if not request.user.has_perm("my_app.add_marks"):
        raise PermissionDenied

    if request.method == "POST":

        form = MarksForm(
            request.POST,
            user=request.user
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Marks Added Successfully"
            )
            return redirect("view_marks")

    else:
        form = MarksForm(
            user=request.user
        )

    return render(
        request,
        "marks/add.html",
        {"form": form}
    )

@login_required
def view_marks(request):

    if not request.user.has_perm("my_app.view_marks"):
        raise PermissionDenied

    if request.user.groups.filter(name="Teachers").exists():

        teacher = request.user.teachers

        teacher_classes = Subjects.objects.filter(
            teacher=teacher
        ).values_list('school_class_id', flat=True)

        get_mrk = Marks.objects.filter(
            student__school_class_id__in=teacher_classes
        )

    else:
        # Admin
        get_mrk = Marks.objects.all()

    return render(
        request,
        'marks/list.html',
        {'get_mrk': get_mrk}
    )

@login_required
def detail_marks(request,id):

    if not request.user.has_perm("my_app.view_marks"):
        raise PermissionDenied

    get_mrk=Marks.objects.filter(id=id).first()

    return render(request,'marks/detail.html',{'get_mrk':get_mrk})

@login_required
def update_marks(request,id):
    if not request.user.has_perm("my_app.update_marks"):
            raise PermissionDenied
    try:
        get_mrk=Marks.objects.get(id=id)
    except Marks.DoesNotExist:

     return redirect('view_marks')

    if request.method=="POST":
        form=MarksForm(request.POST,instance=get_mrk)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Updated Successfully')
            return redirect('view_marks')
    else:
        form=MarksForm(instance=get_mrk)
    return render (request,'marks/add.html',{'form':form})    

@login_required
def delete_marks(request,id):
    if not request.user.has_perm("my_app.delete_marks"):
            raise PermissionDenied

    try:
        get_mrk=Marks.objects.get(id=id)
    except Marks.DoesNotExist:
        return redirect('list_marks')

    if request.method=='POST':
        get_mrk.delete()
        messages.success(request,'marks deleted successfully')
        return redirect('view_marks')
    return render(request,"marks/delete.html",{"get_mrk": get_mrk})

 