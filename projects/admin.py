from django.contrib import admin
from .models import *

class ProjectsImagesInline(admin.TabularInline):  # Use admin.StackedInline for a different layout
    model = ProjectsImages
    extra = 0
    
@admin.register(ProjectsCategory)
class ProjectsCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'client_name', 'date', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectsImagesInline]

@admin.register(ProjectsImages)
class ProjectsImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
