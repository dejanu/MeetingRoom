from django.contrib import admin

#class import from models
from . models import Room
# Register your models here.
admin.site.register(Room)