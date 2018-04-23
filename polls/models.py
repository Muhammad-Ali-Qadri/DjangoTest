from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Room(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    room_number = models.IntegerField(help_text="Enter the room number")
    room_type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)

    ROOM_STATUS = (
        ('o', 'Occupied'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=ROOM_STATUS, help_text="room availability", blank=True)

    class Meta:
        ordering = ["room_number"]

    def __str__(self):
        return str(self.room_number)


class Type(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, help_text="Type name of the room", blank=True)
    capacity = models.IntegerField(help_text="Number of people that can stay")
    price = models.IntegerField(help_text="Price for one night")
    description = models.CharField(max_length=200, help_text="Description of the room", blank=True)
    has_wifi = models.BooleanField(default=False)
    has_dryer = models.BooleanField(default=False)
    has_room_service = models.BooleanField(default=False)
    has_breakfast = models.BooleanField(default=False)
    has_air_conditioning = models.BooleanField(default=False)
    has_spa = models.BooleanField(default=False)
    has_mini_bar = models.BooleanField(default=False)
    has_gym = models.BooleanField(default=False)
    has_pool = models.BooleanField(default=False)
    has_electronic_safe = models.BooleanField(default=False)


    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


class Images(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    room_type_id = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)
    image = CloudinaryField(blank=True, help_text="Add room image")
    description = models.CharField(max_length=100, help_text="Description of the image", blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return str(self.id)


class RestaurantUser(models.Model):
    # fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, help_text="Type name of the room", blank=True)
    email = models.EmailField(help_text="Email address of user")
    password = models.CharField(max_length=20, help_text="password of user", blank=True)

    USER_TYPE = (
        ('u', 'User'),
        ('a', 'Admin'),
    )

    user_type = models.CharField(max_length=1, choices=USER_TYPE, help_text="User type", blank=True)

    class Meta:
        ordering = ["user_type", "id"]

    def __str__(self):
        return self.name


class Registration(models.Model):
    # fields
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('RestaurantUser', on_delete=models.SET_NULL, null=True)
    occupants = models.IntegerField(help_text="number of people staying")
    check_in_date = models.DateTimeField(help_text="Date of check in")
    check_out_date = models.DateTimeField(help_text="Date of check out")
    payment = models.IntegerField(help_text="total expense of rooms")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.user_id.name


class RegistrationDetails(models.Model):
    # fields
    id = models.AutoField(primary_key=True)
    registration_id = models.ForeignKey('Registration', on_delete=models.SET_NULL, null=True)
    room_id = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return str(self.registration_id)


class Review(models.Model):
    # fields
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('RestaurantUser', on_delete=models.SET_NULL, null=True)
    room_id = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(help_text="Rating from 1 to 5")
    review = models.CharField(max_length=200, help_text="Review description", blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.user_id.name
