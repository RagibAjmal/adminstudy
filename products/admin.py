from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.

from .models import Category,Products

admin.site.register(Category)
admin.site.register(Products)
