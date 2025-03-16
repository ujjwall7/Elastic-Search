from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index, name="index"),
    path('about/',views.about, name="about"),
    path('services/',views.services, name="services"),
    path('projects/',views.projectsPage, name="projects"),
    path('blogs/',views.blogsPage, name="blogs"),
    path('contact_form/',views.contact, name="contact_form"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
