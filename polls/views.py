from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def index(request):
    return render(request, "web/index.html", {})


def facilities(request):
    return render(request, "web/facilities.html", {})


def restaurant(request):
    return render(request, "web/restaurant.html", {})


def contact(request):
    return render(request, "web/contact.html", {})


def login(request):
    return render(request, "web/login.html", {})


def signup(request):
    return render(request, "web/signup.html", {})


# SIGNING IN FORM FUNCTION
def signup_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = RestaurantUser()
            user.name = form.cleaned_data['name']
            user.email = form.cleaned_data['email']
            user.password = form.cleaned_data['password']
            user.user_type = 'u'
            user.save()
            request.session['user_id'] = user.id
            return render(request, "web/index.html", {})
        else:
            pass

    else:
        pass
    # TODO: add things to elses
    return render(request, "web/index.html", {})
