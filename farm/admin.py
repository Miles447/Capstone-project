from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Animal, Produce

admin.site.register(Animal)
admin.site.register(Produce)
