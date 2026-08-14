from django.contrib import admin
from .models import Students,Teachers,SchoolClass,Subjects,Attendence,Marks,Parents

admin.site.register(Students)
admin.site.register(Teachers)
admin.site.register(SchoolClass)
admin.site.register(Subjects)
admin.site.register(Attendence)
admin.site.register(Marks)
admin.site.register(Parents)