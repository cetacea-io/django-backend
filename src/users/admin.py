from django.contrib import admin

from .models import User
from accounts.models import Profile

class CustomUserInline(admin.StackedInline):
    model = Profile
    can_delete = True

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (CustomUserInline, )