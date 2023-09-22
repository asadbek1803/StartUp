from django.contrib import admin
from .models import Staff, Album, Services, Blog, Message_to_Admin

# Register your models here.

admin.site.register([Staff, Album, Services, Blog, Message_to_Admin])


