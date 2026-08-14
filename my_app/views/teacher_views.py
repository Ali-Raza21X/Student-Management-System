from django.shortcuts import render,redirect
from..forms import TeacherForm
from django.contrib.auth.decorators import login_required
from ..models import Teachers
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.core.exceptions import PermissionDenied

@login_required
def teacher_dashboard(request):
    return render(
        request,
        "teachers/dashboard.html"
    )

@login_required
def add_teacher(request):
    if not request.user.has_perm("my_app.add_teacher"):
     raise PermissionDenied
    if request.method=="POST":
        form=TeacherForm(request.POST)
        if form.is_valid():
            teacher=form.save()
            user = User.objects.create_user(
            username=f"teacher{teacher.employee_id}",
            password="12345"
            )
            teacher.user = user
            teacher.save()

            group = Group.objects.get(name="Teachers")
            user.groups.add(group)

            messages.success(request, "Teacher Added Successfully")
            return redirect('view_teachers')
            
        else:
            messages.error(request, "Invaild Creadentials Try Again")
    else:
            form=TeacherForm()
            

    return render(request,'teachers/add.html',{'form':form})

@login_required
def view_teachers(request):
    if not request.user.has_perm("my_app.view_teacher"):
        raise PermissionDenied
    teacher_list= Teachers.objects.all()
    context={
        'teacher_list':teacher_list
    }
    return render(request,'teachers/list.html',context)

@login_required
def view_detail(request,employee_id):

    if not request.user.has_perm("my_app.view_detail"):
        raise PermissionDenied
    teacher_detail=Teachers.objects.filter(employee_id=employee_id).first()
    context={"teacher_detail":teacher_detail}
    return render(request,'teachers/detail.html',context)

@login_required
def search_teacher(request):
    employee_id = request.GET.get("search")

    
    if not employee_id:
        return render(request, "teachers/list.html")

    try:
        employee_id = int(employee_id)
    except (TypeError, ValueError):
        return render(request, "teachers/list.html", {
            "message": "Please enter a valid ID."
        })

    teacher_list = Teachers.objects.filter(employee_id=employee_id)

    if teacher_list.exists():
        return render(request, "teachers/list.html", {
            "teacher_list": teacher_list
        })

    return render(request, "teachers/list.html", {
        "message": f"No record found for this id  {employee_id}"
    })
 
@login_required
def update_teacher(request, employee_id):

    if not request.user.has_perm("my_app.update_teacher"):
         raise PermissionDenied
    # Get the teacher record
    try:
        teacher = Teachers.objects.get(employee_id=employee_id)
    except Teachers.DoesNotExist:
        return redirect("view_teachers")

    # Form submitted
    if request.method == "POST":

        # Fill form with submitted data and existing teacher
        form = TeacherForm(request.POST, instance=teacher)

        # Validate and save
        if form.is_valid():
            form.save()
            messages.success(request, "Teacher updated successfully.")
            return redirect("view_teachers")

    # First time opening the page (GET)
    else:
        form = TeacherForm(instance=teacher)

    # Show the form (GET or invalid POST)
    return render(
        request,
        "teachers/add.html",
        {
            "form": form
        }
    )

@login_required
def delete_teacher(request,employee_id):
 if not request.user.has_perm("my_app.delete_teacher"):
      raise PermissionDenied
 try:
        teacher = Teachers.objects.get(employee_id=employee_id)
 except Teachers.DoesNotExist:
            return redirect('view_teachers')
 if request.method == "POST":
          teacher.delete()

          messages.success(request,'Teacher deleted successfully')
          return redirect('view_teachers')
 return render(request,"teachers/delete.html",{"teacher": teacher})
 