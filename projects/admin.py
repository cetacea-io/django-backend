from django.contrib import admin

from .models import Project, Comment, Position

# Register your models here.
class PositionInline(admin.TabularInline):
    model = Position

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        PositionInline
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
