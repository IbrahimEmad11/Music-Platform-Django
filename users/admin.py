from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import UserForm

class UserAdmin( admin.ModelAdmin ):
    form = UserForm
    
admin.site.register(User, UserAdmin)
