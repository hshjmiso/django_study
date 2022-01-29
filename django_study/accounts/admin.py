from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

user = User.objects.first()

user.Profile

Profile.objects.get(user=user)