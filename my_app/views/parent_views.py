from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from..forms import AttendenceForm
from django.contrib.auth.decorators import login_required
from ..models import Attendence,Subjects
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from ..models import Parents, Attendence, Marks
@login_required
def parent_dashboard(request):
    parent = request.user.parents

    return render(
        request,
        "parents/dashboard.html",
        {"parent": parent}
    )


@login_required
def parent_attendance(request):
    parent = request.user.parents

    attendance = Attendence.objects.filter(
        student=parent.student
    )

    return render(
        request,
        "parents/attendance.html",
        {
            "attendance": attendance,
            "student": parent.student
        }
    )


@login_required
def parent_marks(request):
    parent = request.user.parents

    marks = Marks.objects.filter(
        student=parent.student
    )

    return render(
        request,
        "parents/marks.html",
        {
            "marks": marks,
            "student": parent.student
        }
    )


@login_required
def parent_report_card(request):
    parent = request.user.parents
    student = parent.student

    marks = Marks.objects.filter(student=student)
    attendance = Attendence.objects.filter(student=student)

    return render(
        request,
        "parents/report_card.html",
        {
            "student": student,
            "marks": marks,
            "attendance": attendance
        }
    )