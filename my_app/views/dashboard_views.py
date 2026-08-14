from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from ..models import Students,Teachers,SchoolClass,Subjects

def home(request):
    return render (request,'index.html')

@login_required
def admin_dashboard(request):
    
    student_count=Students.objects.count()
    recent_student=Students.objects.order_by('-create_at')[:5]


    teacher_count=Teachers.objects.count()
    recent_teacher=Teachers.objects.order_by('-date_joined')[:5]


    classes_count=SchoolClass.objects.count()
    
    subjects_count=Subjects.objects.count()


    context={
                        
    "student_count":student_count,
    "recent_student":recent_student,
    "teacher_count":teacher_count,
    "recent_teacher":recent_teacher,
    "classes_count":classes_count,
    "subjects_count":subjects_count
}
    return render(request,'dashboard/admin_dashboard.html',context)

@login_required
def dashboard(request):


    user = request.user

    if user.groups.filter(name="Students").exists():
        return redirect("student_dashboard")

    if user.groups.filter(name="Teachers").exists():
        return redirect("teacher_dashboard")

    if user.groups.filter(name="Admin").exists():
        return redirect("admin_dashboard")

    if user.groups.filter(name="Parents").exists():
       return redirect("parent_dashboard")
    else:
     return redirect("home")

@login_required
def parent_dashboard(request):

    parent = request.user.parents

    return render(
        request,
        "parents/dashboard.html",
        {"parent": parent}
    )