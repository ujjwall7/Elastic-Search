from django.contrib import admin

from django.contrib import admin
from.models import *

@admin.register(Category)
class CategoryDisplay(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Tags)
class TagsDisplay(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Comments)
class CommentsDisplay(admin.ModelAdmin):
    list_display = ('name', )
    
@admin.register(Author)
class AuthorDisplay(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Blog)
class BlogDisplay(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Translate)

    