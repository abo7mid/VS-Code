from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def register(reqeust):
    return HttpResponse( "placeholder for users to create a new user record")

def login(reqeust):
    return HttpResponse( "placeholder for users to log in")

def users(reqeust):
    return HttpResponse( "placeholder to later display all the list of users")


