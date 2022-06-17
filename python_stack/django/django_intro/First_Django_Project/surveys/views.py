from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def surveys(request):
    return HttpResponse("placeholder to display all the surveys created")

def new_surveys(request):
    return HttpResponse("placeholder for users to add a new survey")