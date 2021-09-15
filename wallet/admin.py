from django.contrib import admin
from .models import post
from .models import photos

# Register your models here.

admin.site.register(photos)
admin.site.register(post)

