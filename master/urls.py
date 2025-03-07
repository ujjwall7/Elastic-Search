from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name="index"),
    path('about/',views.about, name="about"),
    path('services/',views.services, name="services"),
    path('projects/',views.projects, name="projects"),
    path('blogs/',views.blogs, name="blogs"),
    path('contact/',views.contact, name="contact"),
    path('contact_form/',views.contact_form, name="contact_form"),
]