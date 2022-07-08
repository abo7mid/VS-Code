from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from Favorite_Book_app.models import Book, User
from django.contrib import messages
import bcrypt

# Create your views here.


def index(request):
    if request.method == "POST":

        if request.POST.get("register"):
            print("registration")
            errors = User.objects.validate(request.POST)
            if len(errors) > 0:
                print(errors)
                print(type(request.POST['password']))
                print(request.POST['confirmPassword'])
                for key, value in errors.items():
                    messages.error(request, value)
                    return redirect('/')
            else:
                user = User()
                password = request.POST.get('password')
                user.firstname = request.POST['firstname']
                user.lastname = request.POST['lastname']
                # user.username = request.POST['username']
                user.email = request.POST['email']
                user.password = bcrypt.hashpw(
                    password.encode(), bcrypt.gensalt()).decode()
                user.save()
                messages.success(request, "User created successfully")
                return redirect('/')

        if request.POST.get("login"):
            print("login")
            if not request.POST.get('loginemail'):
                messages.error(request, "Email is empty")
                return redirect('/')
            try:
                user = User.objects.get(email=request.POST['loginemail'])
            except User.DoesNotExist:
                messages.error(request, "Email is not registered!")
                return redirect('/')
            print(user.password)
            if bcrypt.checkpw(request.POST['loginpassword'].encode(), user.password.encode()):
                # request.session["logged_in"] = "successfully registered and logged in!"
                request.session["userId"] = user.id

                return redirect('/books')
            else:
                messages.error(request, "password invalid")
                return redirect('/')
    return render(request, 'index.html')


def books(request):
    if "userId" not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['userId'])
        books = Book.objects.all()
        # books is now like this
        # books = [
        #     {
        #         "id":12,"title":"Ahmed's book","uploaded_by":1,
        #         "id":13,"title":"Muhammed's book","uploaded_by":2,
        #         "id":13,"title":"Muhammed's book","uploaded_by":2,
        #     }
        # ]
        context = {
            "user": user,
            "books":books,
        }
        if request.method == "POST":
            if request.POST.get('add'):
                errors = Book.objects.validate(request.POST)
                if len(errors) > 0:
                    for key,value in errors.items():
                        messages.error(request,value)
                        print(errors)
                        return redirect('/books')
                else :
                    book = Book()
                    book.title = request.POST.get('title')
                    book.desc = request.POST.get('desc')
                    book.uploaded_by = user # relate the book to the user
                    book.save()
                    book = Book.objects.get(id=book.id,uploaded_by=user) # get recent added book
                    book.users_who_like.add(user) # add current user to the list of users who liked this book
                    return redirect('/books')

			
        return render(request, 'books.html', context)


def viewBook(request,bookId):
    print('viewBook')
    if "userId" not in request.session:
        return redirect('/')
    else:
        for user_books in Book.objects.filter(id=bookId):
            if request.session['userId'] == user_books.uploaded_by.id:
                return redirect(reverse('editBook',kwargs={"bookId":user_books.id}))
            else:
                user = User.objects.get(id=request.session['userId'])
                book = Book.objects.get(id=bookId) # get the book with id that passed through the link
                context = {
                    "user": user, 
                    "book":book, # send the book instance to the template so that you can access users_who_like.all through a for loop
                }
    return render(request,'viewBook.html',context)

def addToFavorite(request,bookId):
    book = Book.objects.get(id=bookId)
    book.users_who_like.add(request.session['userId'])
    for user in book.users_who_like.all(): 
        print(user.id)

    return redirect(reverse('viewBook',kwargs={"bookId":book.id}))


def bookEdit(request,bookId):

    book = Book.objects.get(id=bookId)
    # if book.users_who_like


    context = {
        "title":book.title,
        "desc":book.desc,
        "user":request.session['userId'],
    }
    return render(request,'editBook.html',context)

def logout(request):
    del request.session['userId']
    return redirect('/')
