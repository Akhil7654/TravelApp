from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method=="POST":
        uname=request.POST["username"]
        email=request.POST["email"]
        pswrd=request.POST["password"]
        cpswrd=request.POST["cpassword"]

        if pswrd==cpswrd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"ee username already ond !")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"ee Email already ond !")
            else:
                user=User.objects.create_user(username=uname,email=email,password=pswrd)
                user.save()
                print("User created")
                return redirect("/")

        else:
            messages.info(request,"password match aavnila")
            return redirect("register")

    return render(request,"register.html")


def login(request):
    if request.method=="POST":
        uname2=request.POST["username"]
        pass2=request.POST["password"]
        user=auth.authenticate(username=uname2,password=pass2)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Login scene aayi !")
            return redirect("login")

    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")







