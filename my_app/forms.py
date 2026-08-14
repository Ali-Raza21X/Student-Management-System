from django import forms
from .models import Students,Teachers,SchoolClass,Subjects,Attendence,Marks
from django.core.validators import RegexValidator

class RegisterForm(forms.Form):
    username=forms.CharField(max_length=100)
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class StudentForm(forms.ModelForm):
        phone = forms.CharField(
    max_length=11,
    min_length=11,
    validators=[
        RegexValidator(
            regex=r'^\d{11}$',
            message='Phone number must contain exactly 11 digits.'
        )
    ]
)
        class Meta:
            model=Students
            fields = [
            "roll_no",
            "name",
            "email",
            "phone",
            "school_class",
            "age",
        ]

class TeacherForm(forms.ModelForm):
        phone = forms.CharField(
        max_length=11,
        min_length=11,
        validators=[
            RegexValidator(
                regex=r'^\d{11}$',
                message='Phone number must contain exactly 11 digits.'
            )
        ]
    )
        class Meta:
            model=Teachers
            fields = [
            "employee_id",
            "fullname",
            "email",
            "phone",
            "qualification",
        ]

class ClassForm(forms.ModelForm):
        school_class = forms.CharField(
        max_length=2,
        validators=[
            RegexValidator(
                regex=r'^\d+$',
                message='Class No. must contain numbers only.'
            )
        ]
    )

        section = forms.CharField(
        max_length=1,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z]+$',
                message='Section must contain alphabets only.'
            )
        ]
    )

        room_no = forms.CharField(
        max_length=2,
        validators=[
            RegexValidator(
                regex=r'^\d{1,2}$',
                message='Room No. must contain 1 or 2 digits only.'
            )
        ]
    )
        class Meta:
            model=SchoolClass
            fields='__all__'

class SubjectForm(forms.ModelForm):    
        subject_name = forms.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z ]+$',
                message='Subject name must contain alphabets and spaces only.'
            )
        ]
    )
        class Meta:
            model=Subjects
            fields='__all__'

class AttendenceForm(forms.ModelForm):
       class Meta:
        model = Attendence
        fields = [
            'student',
            'status',
        ]

       def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user and user.groups.filter(name="Teachers").exists():

            teacher = user.teachers

            teacher_classes = Subjects.objects.filter(
                teacher=teacher
            ).values_list('school_class_id', flat=True)

            self.fields['student'].queryset = Students.objects.filter(
                school_class_id__in=teacher_classes
            )

            
class MarksForm(forms.ModelForm):

    class Meta:
        model = Marks
        fields = [
            'student',
            'subject',
            'exam_name',
            'obtain_marks',
            'total_marks',
        ]
    def clean(self):
        cleaned_data = super().clean()

        obtain_marks = cleaned_data.get('obtain_marks')
        total_marks = cleaned_data.get('total_marks')

        if obtain_marks is not None and total_marks is not None:
            if obtain_marks > total_marks:
                self.add_error(
                    'obtain_marks',
                    'Obtained marks cannot be greater than total marks.'
                )

        return cleaned_data
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user and user.groups.filter(name="Teachers").exists():

            teacher = user.teachers

            # Only subjects taught by this teacher
            self.fields['subject'].queryset = Subjects.objects.filter(
                teacher=teacher
            )

            # Only students belonging to classes taught by this teacher
            teacher_classes = Subjects.objects.filter(
                teacher=teacher
            ).values_list('school_class_id', flat=True)

            self.fields['student'].queryset = Students.objects.filter(
                school_class_id__in=teacher_classes
            )
        