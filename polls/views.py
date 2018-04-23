from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
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


def login(request):
    return render(request, "web/login.html", {})


def signup(request):
    if request.method == 'POST':
        user = RestaurantUser()
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.user_type = 'u'
        user.save()
        request.session['user_id'] = user.id
        return render(request, "web/index.html", {})
    else:
        return render(request, "web/signup.html", {})
