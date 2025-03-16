from django.shortcuts import render
from urllib.request import urlopen
import requests
import json

from django.http import JsonResponse
from django.core.mail import send_mail
import re
from . models import *
from blogs . models import *
from projects.models import *

from django.db.models import Q
from django.core.paginator import Paginator


# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip

# def get_country_and_ip(request):
#     ip_address = get_client_ip(request)
#     print(f"{ip_address = }")

#     try:
#         response = requests.get(f"http://ip-api.com/json/{ip_address}")
#         response.raise_for_status()
#         print(f"{response = }")
#         data = response.json()
#         print(f"{data = }")
#         country = data.get("countryCode")
#         print(f"{country = }")
#         return country

#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching IP information: {e}")
#         return None
#     except (ValueError, KeyError):
#         print("Error parsing IP information")
#         return None
#     except Exception as e:
#         print(f"An unknown error occurred: {e}")
#         return None

def get_country(request):
    # country = get_country_and_ip(request)
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data =json.load(response)
    country = data.get('country')
    return country if country else None

def getGlobalContext(request):
    context = {}
    country = get_country(request)
    context['country_code'] = country.upper() if country else None
    context['all_blogs'] = Blog.objects.all().order_by('-id')

    context['category'] = Category.objects.all()
    context['all_projects'] = Projects.objects.all().order_by('-id')

    context['fb'] = SocialMedia.objects.filter(social_media = 'Facebook').last()
    context['ig'] = SocialMedia.objects.filter(social_media = 'Instagram').last()
    context['li'] = SocialMedia.objects.filter(social_media = 'Linkedin').last()
    context['tw'] = SocialMedia.objects.filter(social_media = 'Twitter').last()
    context['ytube'] = SocialMedia.objects.filter(social_media = 'Youtube').last()
    context['telg'] = SocialMedia.objects.filter(social_media = 'Telegram').last()
    context['whatsapp'] = SocialMedia.objects.filter(social_media = 'Whatsapp').last()
    context['threads'] = SocialMedia.objects.filter(social_media = 'Threads').last()

    # Projects
    context['projects'] = Projects.objects.all().order_by('-id')
    context['section_projects'] = Section.objects.filter(section_type = 'Projects').last()
    # context['heading_country'] = Heading.objects.filter(heading_type = 'Country').last()

    # Blogs
    context['blogs'] = Blog.objects.all().order_by('-id')
    context['blogs_section'] = Section.objects.filter(section_type = 'Blogs').last()

    return context

def index(request):
    context = getGlobalContext(request)
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def projectsPage(request):
    context = getGlobalContext(request)
    category = request.GET.get('category')
    if category: 
        projects   = Projects.objects.filter(category__slug=category).order_by('-id')  
    else:
        projects = Projects.objects.all().order_by('-id')  
    
    paginator   =   Paginator(projects,10)
    page_number =   request.GET.get('page')
    page_obj    =   paginator.get_page(page_number)
    total_page  =   page_obj.paginator.num_pages
    context['get_category'] = category
    context['projects'] = page_obj
    return render(request, "projects.html", context)

def blogsPage(request):
    context = getGlobalContext(request)
    category = Category.objects.all()
    for x in category:
        x.count = Blog.objects.filter(category = x).count()

    tags = Tags.objects.all()
    for x in tags:
        x.count = Blog.objects.filter(tags = x).count()

    cat_id  =   request.GET.get('cat')
    tags_id = request.GET.get('tags')
    keyword = request.GET.get('keyword')

    print(cat_id)  
    if cat_id:
        blogs   = Blog.objects.filter(category__slug=cat_id).order_by('-id')
    elif tags_id:
        blogs   = Blog.objects.filter(tags__slug=tags_id).order_by('-id')
    elif keyword:
        blogs   = Blog.objects.order_by('-date').filter(Q(category__name__icontains = keyword) | Q(title__icontains=keyword) | Q(short_description__icontains=keyword))
    else:
        blogs = Blog.objects.all().order_by('-id')
    
    paginator   =   Paginator(blogs,1)
    page_number =   request.GET.get('page')
    page_obj    =   paginator.get_page(page_number)
    total_page  =   page_obj.paginator.num_pages

    context['popular'] = Blog.objects.filter(is_popular = True).order_by('-id')
    context['blogs_categories'] = category
    context['blogs_tags'] = tags
    context['blogs']   = page_obj
    context['keyword'] = keyword
    context['cat_id']  = cat_id
    context['tags_id'] = tags_id
    return render(request, "blogs.html", context)

def contact(request):
    if  request.method=="POST":
        print("Called")
        name=request.POST['name']
        email=request.POST['email']
        country_code=request.POST['country_code']
        phone=request.POST['phone']
        subject=request.POST['subject']
        message=request.POST['message']

        print(f"{name = }\n,{email = }\n,{country_code = }\n,{phone = }\n,{subject = }\n,{message = }")

        phone_pattern = r'^[0-9]{10}$'

        if not re.match(phone_pattern, phone):
            return JsonResponse({'success': False, 'message': 'Invalid phone number.<br>Please enter a valid 10-digit phone number.', 'color_class': 'error-toast'})
        
        phone = str(country_code) + ' ' + str(phone)
        new_email=ContactForm(email=email,name=name,message=message,phone=phone, subject=subject)
        new_email.save()

        try:
            email_password = Company.objects.all().last()
            if email_password:
                email_host_user = email_password.gmail_email
                email_host_password = email_password.password
                try:
                    send_mail('Enquiry Received',                                               #Subject Email
                            f'Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}',    #Message Email
                            email_host_user,                                                        #from email
                            [email_host_user,],                                                    #To email
                            fail_silently=False,
                            auth_user=email_host_user,
                            auth_password=email_host_password,
                        )
                except Exception as e:
                    print(e)
                    pass
            return JsonResponse({'success': True, 'message': 'Your request has been received!<br>We will get in touch with you shortly.', 'color_class' : 'success-toast'})
        except Exception as e:
            print(e)
            return JsonResponse({'success': False, 'message': str(e), 'color_class': 'error-toast'})
    else:
        context = getGlobalContext(request)
        context['seo_contact'] = SEO.objects.filter(page_type = 'Contact').last()
        return render(request, "contact.html", context)


















