from django.contrib import admin

from .models import Place, Picture

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    pass