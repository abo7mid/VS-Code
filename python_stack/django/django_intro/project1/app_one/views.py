from django.shortcuts import render, HttpResponse ,redirect
from django.http import JsonResponse


# this function is invoked by whoever request '/' route
# the name parameter is passed using path function in urls module
# the request parameter: Every function's first argument will be the request object
def index(request,name):  
    return HttpResponse("this is the equivalent of @app.route('/')!")


def login(request): # this function is invoked by whoever requests '/login' route, see urls
    return HttpResponse("this is the equivalent of @app.route('/login')!")


# when redirecting, you should provide the whole path, starting with the first /.
def another_method(request):
    return redirect("/redirected_route")


def redirected_method(request):
    return JsonResponse({"response":"JSON response from redirected_method","status":True})


    # path('another_route',views.another_method),
    # path('redirected_route',views.redirected_method)
    
