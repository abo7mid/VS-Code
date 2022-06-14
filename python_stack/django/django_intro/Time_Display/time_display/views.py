from django.shortcuts import render
from time import gmtime, strftime
# Create your views here.


def index(request):
    context = {
        "date": strftime("%Y-%m-%d", gmtime()),
        "time": strftime("%H:%M %p")
    }

    return render(request, "index.html", context)
