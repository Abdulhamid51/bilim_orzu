from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models

from main.models import Contact

from .models import *
from .forms import *
# Register your models here.


admin.site.register(BrithDays)
admin.site.register(Teacher)
admin.site.register(Contact)