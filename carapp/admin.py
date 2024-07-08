from django.contrib import admin
from .models import Car,Savat

admin.site.register(Car)
admin.site.register([Savat])