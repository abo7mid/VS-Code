import email
from django.http import HttpResponse
from django.shortcuts import redirect, render
from app_one.models import User
from django.contrib import messages
import bcrypt

# Create your views here.


def index(request):
    if request.method == "POST":
        if request.POST.get("register"):
            print("registration")
            errors = User.objects.validate(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                    return redirect('/')
            else:
                if User.objects.filter(email=request.POST['email']):
                    messages.error(request,"Email exists!")
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
            if not request.POST['loginemail']:
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

                return redirect('/success')
            else:
                messages.error(request, "password invalid")
                return redirect('/')
    return render(request, 'index.html')


def success(request):
    if "userId" not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['userId'])
        context = {
            "user": user,
            # "loggedin":request.session["logged_in"],
        }
        return render(request, 'success.html', context)


def logout(request):
    del request.session['userId']
    return redirect('/')
