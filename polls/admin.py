from django.contrib import admin
from .models import *
from django import forms
# Register your models here.

admin.site.register(Type)
admin.site.register(RestaurantUser)
admin.site.register(Registration)
admin.site.register(RegistrationDetails)


# admin class for defining room interface
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type')
    pass


# display form for adding images
class AdminImagesForm(forms.ModelForm):
    class Meta:
        fields = ['Image', 'room_type_id', 'description']
        widgets = {
            'Image': forms.ImageField()
        }


# admin class for defining images interface
@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    form = AdminImagesForm
