from django.db import models


def rename_file(instance, filename):
    if filename.find('.') >= 0:
        dot_index = (len(filename) - filename.rfind('.', 1)) * (-1)
        filename = filename[0:dot_index]
    filename = '{}.{}'.format(filename, 'webp')
    return filename

class Company(models.Model):
    company_name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    alternative_phone = models.CharField(max_length=15, null=True)
    google_map_url = models.CharField(max_length=1000, null=True, blank=True)
    favicon_icon=models.ImageField(upload_to=rename_file, null=True)
    logo_icon=models.ImageField(upload_to=rename_file, null=True)
    address = models.TextField(blank=True, null=True)
    footer_description = models.TextField(blank=True, null=True)
    footer_image = models.ImageField(upload_to=rename_file, null=True)
    country_code = models.CharField(max_length=10, null=True)
    gmail_email = models.EmailField(verbose_name='Email (Send Mail)', null=True, blank=True)
    password=models.CharField(max_length=350,verbose_name='Password (Send Mail)', blank=True)
    office_hours = models.CharField(max_length=150, null=True)
    def __str__(self) -> str:
        return f"company id-{self.id}"
    
class SocialMedia(models.Model):
    TypesOfSocialMedia = (('Facebook','Facebook'),('Instagram','Instagram'),('Linkedin','Linkedin'),
                            ('Twitter','Twitter'),('Youtube','Youtube'),('Telegram','Telegram'),
                            ('Whatsapp','Whatsapp'),('Threads','Threads'))
    social_media = models.CharField(max_length=100, choices=TypesOfSocialMedia, null=True)
    url = models.URLField(null=True)

    def __str__(self):
        return self.social_media
    
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=15)
    message = models.TextField()

class SEO(models.Model):
    TypesOfPage = (('Home','Home'), ('About','About'), ('Blogs','Blogs'), ('FAQ','FAQ'), ('Pricing','Pricing'), 
                   ('Contact','Contact'),)
    page_type = models.CharField(max_length=20, choices=TypesOfPage, null=True)
    meta_title  = models.TextField(max_length=500,null=True, blank=True)
    meta_description  = models.TextField(max_length=500,null=True, blank=True)
    meta_keywords  = models.TextField(max_length=500,null=True, blank=True)
    canonical_tag  = models.TextField(max_length=500,null=True, blank=True)
    
    def __str__(self):
        return self.page_type

class Section(models.Model):
    TypesOfSection = (('Blogs','Blogs'), ('Projects','Projects'))
    section_type = models.CharField(max_length=150, choices=TypesOfSection, null=True)
    show = models.BooleanField(default=True)



