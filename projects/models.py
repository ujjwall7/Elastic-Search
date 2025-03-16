from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


def rename_file(instance, filename):
    if filename.find('.') >= 0:
        dot_index = (len(filename) - filename.rfind('.', 1)) * (-1)
        filename = filename[0:dot_index]
    filename = '{}.{}'.format(filename, 'webp')
    return filename

class SEO(models.Model):
    meta_title  = models.TextField(max_length=500,null=True, blank=True)
    meta_description  = models.TextField(max_length=500,null=True, blank=True)
    meta_keywords  = models.TextField(max_length=500,null=True, blank=True)
    canonical_tag  = models.TextField(max_length=500,null=True, blank=True)

    class Meta:
        abstract = True  

class ProjectsCategory(SEO):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=rename_file, null=True)
    slug = models.SlugField(unique=True,blank=True, null=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.title

class ProjectsImages(models.Model):
    project = models.ForeignKey("Projects",  on_delete=models.PROTECT,null=True)
    image = models.ImageField(upload_to=rename_file, null=True)

    def __str__(self):
        return str(self.id)

class Projects(SEO):
    category = models.ForeignKey("ProjectsCategory",  on_delete=models.PROTECT,null=True)
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    date = models.DateField(auto_now=True)
    client_name = models.CharField(max_length=500)
    project_link = models.URLField(max_length=200)
    description = RichTextUploadingField()
    thumbnail_image = models.ImageField(upload_to=rename_file)
    slug = models.SlugField(unique=True,blank=True, null=True)

    def __str__(self):
        return self.title









