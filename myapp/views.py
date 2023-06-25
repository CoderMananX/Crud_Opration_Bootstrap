from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages
# Create your views here.


#add student
def addstd(request):
    if request.method == "POST":
        roll = request.POST.get("roll")
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")

        std = Student(
            roll = roll,
            name = name,
            email = email,
            address = address,
            phone = phone
        )
        std.save()
        # messages.success(request,"added successful !!!")
        return redirect("/home")
    return render(request,"addstd.html")

#show students list
def home(request):
    std = Student.objects.all()
    return render(request,"home.html",{'std':std})

#update student page
def update(request,roll):
    std = Student.objects.get(id=roll)
    return render(request,"update.html",{'std':std})

#updated student submit
def do_update(request,id):
    if request.method == "POST":
        roll = request.POST.get("roll")
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")

        std = Student(
            id=id,
            roll=roll,
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        std.save()
        return redirect("/home")
    return render(request,"update.html")

#delete  perticulter student
def delete(request,roll):
    std = Student.objects.get(id=roll)
    std.delete()
    return redirect("/home")