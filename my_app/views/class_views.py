from django.shortcuts import render,redirect
from..forms import ClassForm
from django.contrib.auth.decorators import login_required
from ..models import SchoolClass
from django.contrib import messages
from django.core.exceptions import PermissionDenied

@login_required
def add_class(request):
    if not request.user.has_perm("my_app.add_class"):
            raise PermissionDenied
    if request.method=="POST":
        form=ClassForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Added Successfully')
            return redirect('view_class')
    else:
        form=ClassForm()

    return render(request,'classes/add.html',{"form":form})

@login_required
def view_class(request):
    if not request.user.has_perm("my_app.view_schoolclass"):
        raise PermissionDenied
    class_data=SchoolClass.objects.all()
    context={
        'class_data':class_data
    }
    if class_data.exists():
        return render(request,'classes/list.html',context)
    else:
        messages.error(request,"error no data is here to display")
        return render(request,'classes/list.html')

@login_required
def class_detail(request,id):
    if not request.user.has_perm("my_app.view_schoolclass"):
        raise PermissionDenied
    classs= SchoolClass.objects.filter(id=id).first()
    return render(request,'classes/detail.html',{'classs':classs})

@login_required
def class_update(request,id):
    if not request.user.has_perm("my_app.update_class"):
            raise PermissionDenied

    # get part
    try:
        classs = SchoolClass.objects.get(id=id)
    except SchoolClass.DoesNotExist:
            return redirect('view_class')

# edit and save
    if request.method=="POST":
        form = ClassForm(
    request.POST,
    instance=classs
)

        if form.is_valid():
            form.save()
            messages.success(request,'Class Updates Successfully')
            return redirect("view_class")

    else:
        form = ClassForm(instance=classs)

    return render(request, "classes/add.html", {
        "form": form,
        
    })

@login_required
def class_delete(request,id):
    if not request.user.has_perm("my_app.delete_class"):
            raise PermissionDenied
    try:
            classs = SchoolClass.objects.get(id=id)
    except SchoolClass.DoesNotExist:
                return redirect('view_class')
    if request.method == "POST":
              classs.delete()
    
              messages.success(request,'Class deleted successfully')
              return redirect('view_class')
    return render(request,"classes/delete.html",{'classs':classs})

