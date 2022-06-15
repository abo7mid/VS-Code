from django.shortcuts import redirect, render
from time import gmtime, strftime
# Create your views here.


def index(request):
    if request.method == "GET":
        print(f"a GET request is made {request.GET}")
    if request.method == "POST":
        print(f"a POST request is made {request.POST}")
        val_from_field_one = request.POST['name']
        val_from_field_two = request.POST['age']
        
        print(val_from_field_one)
        print(val_from_field_two)
        
        redirect("/time_display")
    context = {
        "date": strftime("%Y-%m-%d", gmtime()),
        "time": strftime("%H:%M %p")
    }

    return render(request, "index.html", context)
