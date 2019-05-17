from django.contrib import admin

from .models import Course, Location, DateAndTime

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
  
@admin.register(DateAndTime)
class DateAndTimeAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass