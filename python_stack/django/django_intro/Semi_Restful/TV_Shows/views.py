from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages

from TV_Shows.models import Show
# from datetime import date
import datetime
import time


def index(request):
    return redirect(reverse('shows'))


def shows(request):
    context = {
        # extract all the records from a table
        "shows": Show.object.all()
    }       # and send it to the template (index.html), 
            # for loop and display the data
    return render(request, 'Shows.html', context)


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
    if request.method == "GET":
        print("GET")
        try:
            show = Show.object.get(id=id)
            show.delete()
            # show.deleted = True
            #region <soft delete>
                # if we do not want to delete a record: 
                # 
                # add a boolean field in that entry
                # 
                # and set its value (soft delete) to True to indicate deletion 
                # instead of actual (hard delete) by show.delete()
                # 
                # and when reading the record check its field value 
                # 
                # Show.object.get(id=id,mark_deleted=False) 
                # 
                # and those who marked as True will not be shown
            #endregion
            print("record has been deleted successfuly")
            # messages.success(request,"record has been deleted successfuly")
            # return redirect(reverse('shows'))
            return render(request,'Shows.html')
        except Show.DoesNotExist:
            print("show is not exist to delete!")
            return redirect(reverse('shows'))
    print("reached")
    return render(request,'Shows.html')



def addShow(request):
    # print(f"html redirection to {reverse('add')} ")
    return render(request, 'addshow.html')


def createShow(request):
    if request.method == "POST":
        errors = Show.object.validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                request.session["created"] = False
                return redirect(reverse('add'))
        else:
            messages.success(request, "the show has been added successfully")
            request.session["created"] = True

            show = Show()
            show.title = request.POST['title']
            show.network = request.POST['network']
            show.release_date = request.POST['release_date']
            show.desc = request.POST['desc']
            show.save()
            return redirect(reverse('view' ,kwargs={'id':show.id}))
    return redirect(reverse('TEST'))


def editShow(request, id):
    show = Show.object.get(id=id)
    date = str(show.release_date)
    context = {
        "show": show,
        "date": date
    }
    if request.method == "POST":
        errors = Show.object.validator(request.POST)
        if len(errors) > 0:
            print(errors)
            for key, value in errors.items():
                messages.error(request,value)
                request.session["updated"] = False
                return redirect(reverse('edit',kwargs={'id':id}))
        else:
            try:
                # show = Show.object.get(id=id)
                # date = str(show.release_date)
                show.title = request.POST['title']
                show.network = request.POST['network']
                show.release_date = request.POST['release_date']
                show.desc = request.POST['desc']
                show.save()
                messages.success(request, "the show has been updated successfully")
                request.session["updated"] = True
                #return redirect(reverse(f'shows/{id}/view'))
                return redirect(reverse('view',kwargs={'id':id}))

            except Show.DoesNotExist:
                print("show is not exist to edit!")
                return redirect(reverse('shows'))
    return render(request, 'editShow.html', context)

    
    



    
