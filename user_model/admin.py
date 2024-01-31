from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User

@admin.register(User)
class DjshopUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")