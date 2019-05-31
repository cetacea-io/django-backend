from django.contrib import admin

from .models import MainCategory

@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    pass