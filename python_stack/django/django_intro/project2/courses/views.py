from unittest import TextTestRunner
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from courses.models import Course, Description
# Create your views here.


def index(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/')
        else:

            desc = Description()
            desc.DescText = request.POST['desc']
            desc.save()
            course = Course()
            course.courseDesc = desc
            course.courseName = request.POST['name']
            course.save()
            messages.success(request, "course added successfully")
            return redirect('/')
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'index.html', context)


def destroy(request, id):
    try:
        course = Course.objects.get(id=id)
    except Course.DoesNotExist:
        print("course is not found")
        return redirect('/')

    if request.method == "POST":
        print("button clicked")
        if request.POST.get("yes"):
            print("Yes clicked")
            course.delete()
            return redirect('/')
        if request.POST.get("no"):
            print("No clicked")
            return redirect('/')
    context = {
        "course": course,
    }
    return render(request, 'destroy.html',context)
