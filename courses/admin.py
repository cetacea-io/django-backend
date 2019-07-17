from django.contrib import admin, contenttypes

from .models import Course, Location, DateAndTime, CourseClassification, CoverItem

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
  
@admin.register(DateAndTime)
class DateAndTimeAdmin(admin.ModelAdmin):
    pass

@admin.register(CourseClassification)
class CourseClassificationAdmin(admin.ModelAdmin):
    pass

@admin.register(CoverItem)
class CoverItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ['title', 'categories__title']
    filter_vertical = ['categories', 'tags']