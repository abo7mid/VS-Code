from random import randint
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.

global generated_num
def index(request):
    return render(request, 'index.html')


def process(request):

    print("----process start----")

    if request.POST['guess'] == '':
        return HttpResponse("You must enter a value")
    if request.method == "GET":
        return HttpResponse("GET method is not allowd")
    request.session["generated_num"] = randint(1, 5)
    if int(request.POST['guess']) == request.session["generated_num"]:
        print("generated num ",request.session['generated_num'])

        return render(request,"DoesMatch.html")
 
    print("gener",request.session['generated_num'])

    
    context = {
        "guessed_num": int(request.POST['guess']),
        "generated_num": request.session["generated_num"]
    }

    print("----process end----")

    return render(request, "index.html", context=context)
