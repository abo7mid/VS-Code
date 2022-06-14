from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def create_user(request):
        name =  request.POST['name']
        location = request.POST['location']
        langs = request.POST['langs']
        comment = request.POST['comment']
        context = {
                "Tname": name,
                "Tlocation": location,
                "Tlangs": langs,
                "Tcomment": comment
        }
        print(location)
        print(langs)
        print(comment)
        return render(request,"result.html",context)


