from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages

from TV_Shows.models import Show


def index(request):
    return redirect(reverse('shows'))


def shows(request):
    context = {
        # extract all the records from a table
        "shows": Show.object.all()
    }       # and send it to the template, for loop and display the data
    return render(request, 'index.html', context)


def viewShow(request, id):
    try:
        show = Show.object.get(id=id)
    except Show.DoesNotExist:
        print("show is not exist to view!")
        return redirect(reverse('shows'))
    context = {
        "show": show
    }
    return render(request, 'viewShow.html', context)


def deleteShow(request, id):
    # try:
    #     show = Show.object.get(id=id)
    #     # show.delete()
    #     print("deleted")
    # except Show.DoesNotExist:
    #     print("show is not exist to delete!")
    #     return redirect('/shows')
    # return reverse('shows')
    return HttpResponse("It took me half a day to do this assignment, I'll take a break than come back as strong as as horse")

    # return redirect(reverse('confirm'))


def confirm(request, id):
    pass


def addShow(request):
    print(f"html redirection to {reverse('add')} ")
    return render(request, 'addshow.html')


def createShow(request):
    if request.method == "POST":
        errors = Show.object.validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect(reverse('add'))
        else:
            messages.success(request, "the show has been added successfully")
            show = Show()
            show.title = request.POST['title']
            show.network = request.POST['network']
            show.release_date = request.POST['release_date']
            show.desc = request.POST['desc']
            show.save()
            return redirect(reverse('shows'))
    return redirect(reverse('TEST'))


def editShow(request, id):
    if request.method == "POST":
        show = Show.object.get(id=id)
        date = str(show.release_date)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.desc = request.POST['desc']
        show.save()
        request.session["updated"] = True
    try:
        show = Show.object.get(id=id)
        date = str(show.release_date)
        context = {
            "show": show,
            "date": date
        }
        return render(request, 'editShow.html', context)
    except Show.DoesNotExist:
        print("show is not exist to edit!")
        return redirect(reverse('shows'))
