from django.shortcuts import redirect, render
from flask import request
from dojo_ninjas_app.models import Dojos,Ninjas

# Create your views here.
def index(request):
    context = {
    "dojos" : Dojos.objects.all()
    }
    return render(request,'index.html',context)

def create_dojo(request):
    if request.POST.get("addDojo"):
        print('Button is clicked')
        Dojos.objects.create(name=request.POST["name"],city=request.POST["city"],state=request.POST["state"],desc=request.POST["desc"])
        return redirect('/')
    return redirect('/')


def create_ninja(request):
    if request.method == "POST":
        print("POST Method")
        if request.POST.get("addNinja"):
            print("Button Clicked")
            print(request.POST["dojo"])
            obj = Dojos.objects.get(name=request.POST["dojo"])
            Ninjas.objects.create(first_name=request.POST["firstname"],last_name=request.POST["lastname"],dojo=obj)
            return redirect('/')

        if request.POST.get("delete"):
            Dojos.objects.filter(name=request.POST["dojo"]).delete()
            return redirect('/')
    
    return redirect('/')

def templates(request):
    return render(request,"")        

