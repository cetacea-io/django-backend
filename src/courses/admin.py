from django.contrib import admin

from .models import Course, Location

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
  
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass