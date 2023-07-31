from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['re_password']

        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR, "username already exists, please change it!.")
            print("username already exists")

        elif User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR, "email taken, please provide another one!")
            print("e-mail already exists")

        elif password != confirm_password:
            messages.add_message(request, messages.ERROR, "password didn't match")
            print("password invalid")

        else:
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                            email=email, password=password)
            user.save()
            messages.add_message(request, messages.SUCCESS, 'you are registerd !')
            return redirect('estore_app1:home')

    return render(request, 'register.html')


def log_in(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=user_name, password=password)
        print(user)
        #
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, "welcome {}...".format(user_name))
            return redirect('content/home/')

        else:
            messages.add_message(request, messages.ERROR, "invalid username or password!")
            return redirect('/')
    return render(request, 'login.html')


def log_out(request):
    auth.logout(request)
    return redirect('/')
