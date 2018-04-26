from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *


# show images of hotel rooms and direct to index.html
def index(request):
    images = []
    types = Type.objects.all()
    for type in types:
        images.append(type.images_set.first())

    rooms = zip(types, images)
    return render(request, "web/index.html", {'rooms': rooms})


def facilities(request):

    return render(request, "web/facilities.html", {})


def restaurant(request):
    return render(request, "web/restaurant.html", {})


def contact(request):
    return render(request, "web/contact.html", {})


@login_required
def my_logout(request):
    logout(request)
    return render(request, "web/index.html", {})


@login_required
def profile(request):
    return render(request, "web/contact.html", {})


# Login for the user
def my_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin')
            return redirect('/index/')
        else:
            return redirect('/login/')
    else:
        return render(request, "web/login.html", {})


# signup for the user
def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']

        name_arr = name.split(' ')
        firstname = name_arr[0]

        # if valid user
        if len(name_arr) > 1:
            lastname = name_arr[1]
            user = User.objects.create_user(username=username, email=email,
                                            first_name=firstname, last_name=lastname)
            # if user is created
            if user is not None:
                user.set_password(password)
                user.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('/index/')
            else:
                return redirect('/signup/')
        else:
            return redirect('/signup/')
    else:
        return render(request, "web/signup.html", {})
