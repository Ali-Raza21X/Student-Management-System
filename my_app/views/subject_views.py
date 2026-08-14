from django.shortcuts import render,redirect
from..forms import SubjectForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from ..models import Subjects
from django.contrib import messages
from django.core.exceptions import PermissionDenied

@login_required
def add_sub(request):
    if not request.user.has_perm("my_app.add_subject"):
            raise PermissionDenied
    if request.method=='POST':
        form=SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Subject Added Successfully')
            return redirect('view_subject')
    else:
         form=SubjectForm()
    return render(request,'subjects/add.html',{'form':form})

@login_required
def view_sub(request):
    if not request.user.has_perm("my_app.view_subjects"):
        raise PermissionDenied
    get_sub=Subjects.objects.all()
    context={
        'get_sub':get_sub
    }
    return render(request,'subjects/list.html',context)

@login_required
def detail_sub(request,id):
    if not request.user.has_perm("my_app.view_subjects"):
        raise PermissionDenied
    sub=Subjects.objects.filter(id=id).first
    context={
        'sub':sub
    }
    return render(request,'subjects/detail.html',context)

@login_required
def update_sub(request,id):
    if not request.user.has_perm("my_app.update_sub"):
            raise PermissionDenied
    # get part
    try:
        subject = Subjects.objects.get(id=id)
    except Subjects.DoesNotExist:
            return redirect('view_subject')

# edit and save
    if request.method=="POST":
        form = SubjectForm(
    request.POST,
    instance=subject
)

        if form.is_valid():
            form.save()
            messages.success(request,'Subject Updates Successfully')
            return redirect("view_subject")

    else:
        form = SubjectForm(instance=subject)

    return render(request, "subjects/add.html", {
        "form": form
    })

@login_required
def delete_sub(request,id):
     
 if not request.user.has_perm("my_app.delete_subject"):
            raise PermissionDenied
 try:
        subject = Subjects.objects.get(id=id)
 except Subjects.DoesNotExist:
            return redirect('view_subjects')
 if request.method == "POST":
          subject.delete()

          messages.success(request,'Subject deleted successfully')
          return redirect('view_subject')
 return render(request,"subjects/delete.html",{"subject": subject})

