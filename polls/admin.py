from django.contrib import admin
from .models import *
from django import forms
# Register your models here.

admin.site.register(Type)
admin.site.register(RestaurantUser)
admin.site.register(Images)
admin.site.register(Registration)
admin.site.register(RegistrationDetails)


# admin class for defining room interface
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type')
    pass

# # display form for adding images
# class AdminImagesForm(forms.ModelForm):
#     image = forms.ImageField(help_text="Image of room to upload")
#
#     class Meta:
#         fields = '__all__'
#
#
# # admin class for defining images interface
# @admin.register(Images)
# class ImagesAdmin(admin.ModelAdmin):
#     form = AdminImagesForm
#     fieldsets = (
#         (None, {
#             'fields': ('image', 'room_type_id', 'description',),
#         }),
#     )
