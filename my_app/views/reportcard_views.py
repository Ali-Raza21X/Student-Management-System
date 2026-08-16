from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from ..models import Marks,Students,Attendence
from django.core.exceptions import PermissionDenied
@login_required
def report_card(request, id):
    if not (
        request.user.is_superuser
        or request.user.groups.filter(name="Admin").exists()
        or request.user.groups.filter(name="Teachers").exists()
    ):
        raise PermissionDenied

    student = Students.objects.get(id=id)

    marks = Marks.objects.filter(student=student)
    attendance = Attendence.objects.filter(student=student)

    total_days = attendance.count()
    present_days = attendance.filter(status=True).count()
    absent_days = attendance.filter(status=False).count()

    if total_days > 0:
        attendance_percent = (present_days / total_days) * 100
    else:
        attendance_percent = 0

    context = {
        'student': student,
        'marks': marks,
        'total_days': total_days,
        'attendance': attendance,
        'present_days': present_days,
        'absent_days': absent_days,
        'attendance_percent': attendance_percent,
    }

    return render(
        request,
        'report_card/report.html',
        context
    )