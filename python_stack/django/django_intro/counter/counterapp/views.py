from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    if "counter" in request.session:
        counter = request.session["counter"]
    else:
        counter = 0
        counter = request.session["counter"] = 0
    request.session["counter"] = counter +1

    context = {
        "counter":counter
    }
    return render(request,'index.html',context)
def destroy(request):
    if "counter" in request.session:
        del request.session["counter"]

    return redirect("/")