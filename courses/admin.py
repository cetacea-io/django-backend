from django.contrib import admin

# from django_summernote.admin import SummernoteModelAdmin

from .models import Course, Location, DateAndTime

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    # summernote_fields = '__all__'
    pass
  
@admin.register(DateAndTime)
class DateAndTimeAdmin(admin.ModelAdmin):
    # summernote_fields = '__all__'
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # summernote_fields = '__all__'
    pass