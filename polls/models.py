from django.db import models


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

    status = models.CharField(max_length=1, choices=ROOM_STATUS, help_text="room availability")

    class Meta:
        ordering = ["room_number"]

    def __str__(self):
        return self.room_number


class Type(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, help_text="Type name of the room")
    capacity = models.IntegerField(help_text="Number of people that can stay")
    price = models.IntegerField(help_text="Price for one night")
    has_wifi = models.BooleanField()
    has_room_service = models.BooleanField()
    has_breakfast = models.BooleanField()
    has_shuttle_service = models.BooleanField()
    has_spa = models.BooleanField()
    has_mini_bar = models.BooleanField()
    has_gym = models.BooleanField()
    has_pool = models.BooleanField()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


class Images(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    room_type_id = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)
    url = models.URLField(help_text="URL of the stored image")
    description = models.CharField(max_length=100, help_text="Description of the image")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.url


class RestaurantUser(models.Model):
    # fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, help_text="Type name of the room")
    email = models.EmailField(help_text="Email address of user")
    password = models.CharField(max_length=20, help_text="password of user")

    ROOM_STATUS = (
        ('u', 'User'),
        ('a', 'Admin'),
    )

    user_type = models.CharField(max_length=1, choices=ROOM_STATUS, help_text="room availability")

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
        return self.id


class RegistrationDetails(models.Model):
    # fields
    id = models.AutoField(primary_key=True)
    registration_id = models.ForeignKey('Registration', on_delete=models.SET_NULL, null=True)
    room_id = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.id
