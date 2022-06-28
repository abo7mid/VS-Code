import email
from django.http import HttpResponse
from django.shortcuts import redirect, render
from app_one.models import Comment, Message, User
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

                return redirect('/wall')
            else:
                messages.error(request, "password invalid")
                return redirect('/')
    return render(request, 'index.html')




def wall(request):
    if "userId" not in request.session:
        return redirect('/')

    else:
        allmessages = Message.objects.order_by('-created_at') # sort messsages by most recent first
        comments = Comment.objects.all() # this will sort the comments by oldest first
        user = User.objects.get(id=request.session['userId'])
        context = {
            "user": user,
            "messages":allmessages,
            "comments":comments,
        }	
        if request.method == "POST":
            if request.POST.get('postmessage'):
                if not request.POST['message']:
                    messages.error(request, "Write the message first plesae!") 
                    # the above error message will be sent to '/' route (index.html), how to send it to '/wall' route wall.html
                    print("Write the message first plesae!")
                    return redirect('/wall')
            
                else:
                    message = Message()
                    message.user=user
                    message.message=request.POST.get('message')
                    message.save()
                    request.session['messageId'] = message.id
                    # print(message.id,request.POST['message'])

            if request.POST.get('postcomment'):
                if not request.POST['comment']:
                    return redirect('/wall')
                else:
                    comment = Comment()
                    comment.user = user
                    comment.message = Message.objects.get(id=request.POST.get('messageid'))
                    print(request.POST.get('messageid'))
                    comment.comment = request.POST.get('comment')
                    comment.save()

                    comments = Comment.objects.filter(message=request.POST.get('messageid')).last()
                    # print(comment.id,request.POST['comment'])






        return render(request, 'wall.html', context)





def logout(request):
    del request.session['userId']
    return redirect('/')
