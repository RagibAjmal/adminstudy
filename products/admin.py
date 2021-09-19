from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.

from .models import Organizer,Events

admin.site.register(Organizer)
admin.site.register(Events)
