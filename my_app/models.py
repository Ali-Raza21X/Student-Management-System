from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SchoolClass(models.Model):
     school_class=models.CharField( max_length=5)
     section=models.CharField( max_length=5)
     room_no=models.CharField( max_length=10)
     def __str__(self):
      return f"{self.school_class} {self.section}"


class Students(models.Model):
    roll_no=models.IntegerField(blank=False,unique=True)
    name=models.CharField(max_length=100,blank=False)
    email=models.EmailField(max_length=200,blank=False,unique=True)
    phone=models.CharField(max_length=15,blank=False,unique=True)
    user=models.OneToOneField(
          User,on_delete=models.PROTECT,blank=True,null=True
    )
    school_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.PROTECT,
         null=True,
         blank=True
    )
    age=models.PositiveIntegerField(blank=False)
    create_at=models.DateTimeField(max_length=100,auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} {self.school_class}"
    

class Teachers(models.Model):
    employee_id=models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100, blank=False)
    email=models.EmailField(blank=False, max_length=254)
    phone = models.CharField(max_length=11)
    qualification = models.CharField(max_length=100)
    date_joined=models.DateField(auto_now_add=True)
    user = models.OneToOneField(
        User,on_delete=models.PROTECT,blank=True,null=True
    )

    def __str__(self):
            return f"{self.fullname}"


class Subjects(models.Model):
    subject_name = models.CharField(max_length=100)

    school_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.PROTECT
    )

    teacher = models.ForeignKey(
        Teachers,
        on_delete=models.PROTECT
    )
    def __str__(self):
                return f"{self.subject_name}"


class Attendence(models.Model):
    
    student=models.ForeignKey(
        Students,
        on_delete=models.PROTECT
    )
    status=models.BooleanField()
    date=models.DateField(auto_now_add=True)


class Marks(models.Model):
     

     EXAM_CHOICES = [
        ("MID", "Mid Term"),
        ("FINAL", "Final Term"),
    ]
     student=models.ForeignKey(
         Students,
         on_delete=models.PROTECT
     )
     subject=models.ForeignKey(
         Subjects,
         on_delete=models.PROTECT
     )

     exam_name=models.CharField(max_length=35,choices=EXAM_CHOICES)
     obtain_marks=models.IntegerField()
     total_marks=models.IntegerField()
     def __str__(self):
      return f"{self.student}-{self.subject}-{self.exam_name}"


class Parents(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT
    )

    student = models.OneToOneField(
        Students,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f"{self.user.username} - {self.student.name}"
          

     