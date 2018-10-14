from django.contrib import admin

from .models import Project, Comment

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass