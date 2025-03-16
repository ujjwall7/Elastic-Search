from django.contrib import admin
from . models import *


admin.site.register(SocialMedia)

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone','subject']
    list_display_links = ['name', 'email', 'phone','subject']

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'email', 'phone']
    list_display_links = ['id', 'email', 'phone']

@admin.register(SEO)
class SEODisplay(admin.ModelAdmin):
    list_display = ('id', 'page_type')

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'section_type', 'show']
    list_display_links = ['id', 'section_type', 'show']
    