from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from flask import request

from users_app.models import Users



# Create your views here.

def index(request):
    users = Users.objects.all()

    context = {
        "users":users
    }
    return render(request,'index.html',context)


def addUser(request):
    if request.method == "GET":
        return HttpResponse("GET method is not allowd!")

    if request.method == "POST":
        print("button clicked")
        user = Users.objects.create(first_name=request.POST.get("firstname","None"),last_name=request.POST.get("lastname","None"),email=request.POST.get("email","None"),age=request.POST.get("age",0))
        request.session["message"] = f"user {user.id} has been added successfuly!"

        return redirect("/")
    context = {
        "message":request.session.pop("message","")
    }
    return render(request,"indxe.html",context)