from django.contrib import admin
from django.urls import path
from .views import auth_views,dashboard_views,teacher_views,student_views,class_views,subject_views,attendance_views,marks_views,reportcard_views,parent_views


urlpatterns = [
    path('', auth_views.home,name='home'), 
    path('dashboard/', dashboard_views.dashboard,name='dashboard'),
    path('admin/dashboard/',dashboard_views.admin_dashboard,name="admin_dashboard"),
    path('login/', auth_views.user_login,name='login'),
    # path('register/', auth_views.register,name='register'),
    path('logout/', auth_views.logout_view,name='logout'),





    path('students/', student_views.student_list,name='list_student'),
    path('students/add/', student_views.add_student,name='add_student'),
    path('students/search/', student_views.search,name='search'),
    path("students/<int:roll_no>/", student_views.student_detail, name="student_detail"),
    path("students/<int:roll_no>/edit/", student_views.update, name="update_detail"),
    path("students/<int:roll_no>/delete/", student_views.delete, name="delete_detail"),
    path('students/profile/',student_views.student_profile,name='student_profile'),
    path('students/dashboard/',student_views.student_dashboard,name='student_dashboard'),
    path('students/marks/',student_views.student_marks,name='student_marks'),
    path('students/attendance/',student_views.student_attendance,name='student_attendance'),
    path('students/report-card/',student_views.student_report_card,name='student_report_card'),








    path('teachers/',teacher_views.view_teachers,name='view_teachers'),
    path('teachers/add/',teacher_views.add_teacher,name='add_teacher'),
    path('teachers/detail/<int:employee_id>/',teacher_views.view_detail,name='view_detail'),
    path('teachers/search/',teacher_views.search_teacher,name='search_teacher'),
    path('teachers/update/<int:employee_id>/',teacher_views.update_teacher,name='update_teacher'),
    path('teachers/delete/<int:employee_id>/',teacher_views.delete_teacher,name='delete_teacher'),
    path("teachers/dashboard/",teacher_views.teacher_dashboard,name="teacher_dashboard"),


    path('class/',class_views.view_class,name='view_class'),
    path('class/add',class_views.add_class,name='add_class'),
    path('class/detail/<int:id>',class_views.class_detail,name='class_detail'),
    path('class/update/<int:id>',class_views.class_update,name='class_update'),
    path('class/delete/<int:id>',class_views.class_delete,name='class_delete'),


    path('subject/',subject_views.view_sub,name='view_subject'),
    path('subject/add',subject_views.add_sub,name='add_subject'),
    path('subject/detail/<int:id>',subject_views.detail_sub,name='detail_subject'),
    path('subject/update/<int:id>',subject_views.update_sub,name='update_subject'),
    path('subject/delete/<int:id>',subject_views.delete_sub,name='delete_subject'),



    path('attendance/',attendance_views.view_attend,name="view_attend"),
    path('attendance/add',attendance_views.add_attend,name="add_attend"),
    path('attendance/update/<int:id>',attendance_views.update_attend,name="update_attend"),
    path('attendance/delete/<int:id>',attendance_views.delete_attend,name="delete_attend"),
    path('attendance/detail/<int:id>',attendance_views.detail_attend,name="detail_attend"),



    path('marks/',marks_views.view_marks,name="view_marks"),
    path('marks/add',marks_views.add_marks,name="add_marks"),
    path('marks/detail/<int:id>/', marks_views.detail_marks, name='detail_marks'),
    path('marks/update/<int:id>/', marks_views.update_marks, name='update_marks'),
    path('marks/delete/<int:id>/', marks_views.delete_marks, name='delete_marks'),
    path('report-card/<int:id>/',reportcard_views.report_card, name='report_card'),


    path('parent/dashboard/',parent_views.parent_dashboard,name='parent_dashboard'),
    path('parent/attendance/',parent_views.parent_attendance,name='parent_attendance'),
    path('parent/marks/',parent_views.parent_marks,name='parent_marks'),
    path('parent/report-card/',parent_views.parent_report_card,name='parent_report_card'),
   

]
 