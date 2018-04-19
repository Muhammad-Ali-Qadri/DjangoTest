from django.http import HttpResponse
from django.shortcuts import render


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
