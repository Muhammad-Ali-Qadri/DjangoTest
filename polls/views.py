from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *


# show images of hotel rooms and direct to index.html
def index(request):
    if request.user.is_superuser:
        logout(request)

    images = []
    types = Type.objects.all()
    for type in types:
        images.append(type.images_set.first())

    rooms = zip(types, images)
    return render(request, "web/index.html", {'rooms': rooms})


def facilities(request):
    if request.user.is_superuser:
        logout(request)

    return render(request, "web/facilities.html", {})


def restaurant(request):
    if request.user.is_superuser:
        logout(request)

    return render(request, "web/restaurant.html", {})


def contact(request):
    if request.user.is_superuser:
        logout(request)

    return render(request, "web/contact.html", {})


def my_logout(request):
    logout(request)
    return render(request, "web/index.html", {})


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
            return index(request)
        else:
            return render(request, "web/login.html", {'error': 'Invalid Username or Password!'})
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
                return index(request)
            else:
                return render(request, "web/signup.html", {'error': 'Username already in use!'})
        else:
            return render(request, "web/signup.html", {'error': 'Enter full name!'})
    else:
        return render(request, "web/signup.html", {})
