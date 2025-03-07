from django.shortcuts import render
from urllib.request import urlopen
import requests
import json

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_country_and_ip(request):
    ip_address = get_client_ip(request)
    print(f"{ip_address = }")

    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        response.raise_for_status()
        print(f"{response = }")
        data = response.json()
        print(f"{data = }")
        country = data.get("countryCode")
        print(f"{country = }")
        return country

    except requests.exceptions.RequestException as e:
        print(f"Error fetching IP information: {e}")
        return None
    except (ValueError, KeyError):
        print("Error parsing IP information")
        return None
    except Exception as e:
        print(f"An unknown error occurred: {e}")
        return None

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
    print(f"{country = }")
    context['country_code'] = country.upper() if country else None
    return context

def index(request):
    context = getGlobalContext(request)
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def projects(request):
    return render(request, "projects.html")

def blogs(request):
    return render(request, "blogs.html")

def contact(request):
    return render(request, "contact.html")

def contact_form(request):
    return render(request, "contact.html")

















