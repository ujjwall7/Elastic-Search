from django.contrib import admin
from . models import *


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone','subject']
    list_display_links = ['name', 'email', 'phone','subject']
    










