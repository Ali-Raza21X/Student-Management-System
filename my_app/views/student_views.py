from django.shortcuts import render,redirect
from..forms import StudentForm
from django.contrib.auth.decorators import login_required
from ..models import Students,User,Marks,Attendence
from django.contrib import messages
from django.contrib.auth.models import User,Group
from django.core.exceptions import PermissionDenied
from django.db.models import ProtectedError


@login_required
def student_dashboard(request):
    student = request.user.students

    return render(
        request,
        "students/dashboard.html",
        {"student": student}
    )

@login_required
def student_profile(request):
    student = request.user.students

    return render(
        request,
        "students/profile.html",
        {"student": student}
    )

@login_required
def student_marks(request):
    student = request.user.students

    marks = Marks.objects.filter(student=student)

    return render(
        request,
        "students/marks.html",
        {"marks": marks}
    )

@login_required
def student_attendance(request):
    student = request.user.students

    attendance = Attendence.objects.filter(student=student)

    return render(
        request,
        "students/attendance.html",
        {"attendance": attendance}
    )

@login_required
def student_report_card(request):
    student = request.user.students

    marks = Marks.objects.filter(student=student)
    attendance = Attendence.objects.filter(student=student)

    context = {
        "student": student,
        "marks": marks,
        "attendance": attendance,
    }

    return render(
        request,
        "students/report_card.html",
        context
    )

@login_required
def add_student(request):
   if not request.user.has_perm("my_app.add_student"):
    raise PermissionDenied
   if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            student=form.save()
            user = User.objects.create_user(
                username=f"student{student.roll_no}",
                password="12345"
             )
            student.user = user
            student.save()
            group = Group.objects.get(name="Students")
            user.groups.add(group)
            messages.success(request,'Added Succesfully')
            return redirect('list_student')
    
   else:
        form=StudentForm()
    
   return render(request,"students/add_student.html",{"form":form})

@login_required
def student_list(request):
    if not request.user.has_perm("my_app.view_students"):
        raise PermissionDenied

    data=Students.objects.all()
    
    context={
        'data':data
    }
    if data.exists():

        return render(request,'students/student_list.html',context)
    else:
        context={
        'message':"NO Student Found Add A student"}
        return render(request,'students/student_list.html',context)

@login_required
def search(request):

    roll_no = request.GET.get("search")

    
    if not roll_no:
        return render(request, "students/student_list.html")

    try:
        roll_no = int(roll_no)
    except (TypeError, ValueError):
        return render(request, "students/student_list.html", {
            "message": "Please enter a valid roll number."
        })

    data = Students.objects.filter(roll_no=roll_no)

    if data.exists():
        return render(request, "students/student_list.html", {
            "data": data
        })
    else:
        return render(request, "students/student_list.html", {
        "message": f"No record found for roll no {roll_no}"
    })

@login_required
def student_detail(request,roll_no): 
 if not request.user.has_perm("my_app.view_students"):

        raise PermissionDenied
    
 student= Students.objects.filter(roll_no=roll_no).first()
 return render(request,'students/student_detail.html',{'student':student})
    
@login_required
def update(request,roll_no):
    if not request.user.has_perm("my_app.update_detail"):
     
     raise PermissionDenied
# get part
    try:
        student = Students.objects.get(roll_no=roll_no)
    except Students.DoesNotExist:
            return redirect('list_student')

# edit and save
    if request.method=="POST":
        form = StudentForm(
    request.POST,
    instance=student
)

        if form.is_valid():
            form.save()
            messages.success(request,'Student Updates Successfully')
            return redirect("list_student")

    else:
        form = StudentForm(instance=student)

    return render(request, "students/add_student.html", {
        "form": form
    })


@login_required
def delete(request, roll_no):


    if not request.user.has_perm("my_app.delete_detail"):
        raise PermissionDenied

    try:
        student = Students.objects.get(roll_no=roll_no)

    except Students.DoesNotExist:
        return redirect('list_student')

    if request.method == "POST":

        try:
            student.delete()

            messages.success(
                request,
                'Student deleted successfully'
            )

        except ProtectedError:
            messages.error(
                request,
                'This student cannot be deleted because attendance, marks, or other records already exist.'
            )

        return redirect('list_student')

    return render(
        request,
        "students/delete_student.html",
        {"student": student}
    )

