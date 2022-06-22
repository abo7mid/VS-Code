from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book, Author
# Create your views here.


def index(request):
    context = {

        "books": Book.objects.all()
    }

    return render(request, 'index.html', context=context)


# def add_book(request):
#     # pass the post data to the method we wrote and save the response in a variable called errors
#     errors = Book.objects.basic_validator(request.POST)

#     # check if the errors dictionary has anything in it
#     if len(errors) > 0:
#         # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
#         for key, value in errors.items():
#             messages.error(request, value)
#         # redirect the user back to the form to fix the errors
#         return redirect('/')
#     else:
#         # if the errors object is empty, that means there were no errors!
#         # retrieve the blog to be updated, make the changes, and save
#         book = Book.objects.create(title=request.POST['title'],desc=request.POST['desc'])
#         # book.save()
#         messages.success(request, "Book successfully Created")
#         # redirect to a success route
#         return redirect('/')


def add_book(request):
    errors = Book.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        book = Book.objects.create(
            title=request.POST['title'], desc=request.POST['desc'])
        messages.success(request, "Book successfully Created")
        return redirect('/')


def add_author(request):
    if request.method == "POST":
        errors = Author.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/add_author')
        else:
            author = Author.objects.create(
                notes=request.POST["notes"], lastname=request.POST['lastname'], firstname=request.POST['firstname'])
            # author = Author()
            # author.firstname = request.POST['firstname']
            # author.lastname = request.POST['lastname']
            # author.notes = request.POST['notes']
            # author.save()
            messages.success(request, "Author successfully Created")
            return redirect("/authors")
    return redirect('/authors')


def view_book(request, id):
    book = Book.objects.get(id=id)
    authors = Author.objects.all()
    context = {
        "book": book,
        "authors": authors
    }
    return render(request, 'view_book.html', context=context)


def delete_book(request,id):
    Book.objects.filter(id=id).delete()
    print(f"book {id} deleted")
    return redirect("/")


def authors(request):
    context = {

        "authors": Author.objects.all()
    }
    return render(request, 'authors.html', context=context)


def view_author(request, id):
    author = Author.objects.get(id=id)
    books = Book.objects.all()
    context = {
        # "id":id,
        "author": author,
        "books": books
    }
    return render(request, 'view_author.html', context=context)


def delete_author(request,id):
    Author.objects.filter(id=id).delete()
    print(f"Author {id} deleted")
    return redirect("/authors")


def addAuthorToBook(request):
    return redirect('/')

def addBookToAuthor(request):
    return redirect('/')
