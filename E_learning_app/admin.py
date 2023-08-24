from django.contrib import admin
from .models import CustomUser
from .models import Course
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Course)