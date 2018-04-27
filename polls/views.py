from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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


# registered users can review the hotel
@login_required
def review(request):
    # get details entered for review and save them (review is associated with each user)
    if request.method == 'POST':
        rating = request.POST['rating']
        review = request.POST['review_text']
        rev = Review(user_id=request.user, rating=rating, review=review)
        rev.save()
        return redirect('index')
    else:
        return render(request, "web/review.html", {})


@login_required
def my_logout(request):
    logout(request)
    return render(request, "web/index.html", {})


# this view will only be accessed if the user is logged in
@login_required
def profile(request):
    # Get changes in profile and save them in model
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        email = request.POST['email']
        address = request.POST['address']
        new_pic = request.FILES.get('newProfilePic')

        if first_name is not None:
            request.user.first_name = first_name
        if last_name is not None:
            request.user.last_name = last_name
        if password is not None and password != "":
            request.user.set_password(password)
        if email is not None:
            request.user.email = email
        if new_pic is not None:
            request.user.profile.profile_pic = new_pic
        if address is not None:
            request.user.profile.address = address

        request.user.save()
        return redirect('profile')
    else:
        # get the persons previous reviews and bookings to show on template (view)
        return render(request, "web/profile.html", {'reviews': request.user.profile.review_set.all()})


# Login for the user. Authenticate user and if valid, redirect it to main page
def my_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('Admin')
            return redirect('index')
        else:
            return redirect('login')
    else:
        return render(request, "web/login.html")


# signup for the user
def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        profile_pic = request.FILES.get('profile_pic')
        name_arr = name.split(' ')
        firstname = name_arr[0]

        # if valid user
        if len(name_arr) > 1:
            lastname = name_arr[1]
            user = User.objects.create_user(username=username, email=email,
                                            first_name=firstname, last_name=lastname)
            # if user is created save it in database
            if user is not None:
                user.set_password(password)

                if profile_pic is not None:
                    user.profile.profile_pic = profile_pic
                user.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('index')
            else:
                return redirect('signup')
        else:
            return redirect('signup')
    else:
        return render(request, "web/signup.html")
