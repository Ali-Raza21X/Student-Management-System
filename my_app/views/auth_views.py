from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from..forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from ..models import Students, Teachers, SchoolClass, Subjects


def home(request):

    student_count = Students.objects.count()
    teacher_count = Teachers.objects.count()
    classes_count = SchoolClass.objects.count()
    subjects_count = Subjects.objects.count()

    context = {
        "student_count": student_count,
        "teacher_count": teacher_count,
        "classes_count": classes_count,
        "subjects_count": subjects_count,
    }

    return render(request, "index.html", context)

# def register(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             User.objects.create_user(
#                 username=form.cleaned_data["username"],
#                 email=form.cleaned_data["email"],
#                 password=form.cleaned_data["password"],
#             )
#             messages.success(request,'User Registered Successfully')
#             return redirect("login")
#     else:
        
#         form = RegisterForm()

#     # 
#     return render(request, "registration/register.html", {"form": form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                messages.success(request, 'User LoggedIn Successfully')

                if user.is_superuser:
                    return redirect('admin_dashboard')

                return redirect('dashboard')

            else:
                messages.error(request, 'Wrong Credentials. Try Again.')

    else:
        form = LoginForm()

    return render(
        request,
        'registration/login.html',
        {'form': form}
    )

def logout_view(request):

    logout(request)
    messages.success(request,'User Loggedout Successfully')
    return redirect("login")
