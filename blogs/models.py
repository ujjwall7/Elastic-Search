from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

def rename_file(instance, filename):
    if filename.find('.') >= 0:
        dot_index = (len(filename) - filename.rfind('.', 1)) * (-1)
        filename = filename[0:dot_index]
    filename = '{}.{}'.format(filename, 'webp')
    return filename

#---------------BLOGS---------------
class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=rename_file, null=True)
    slug = models.SlugField(unique=True,blank=True, null=True)
    meta_title  = models.TextField(max_length=500,null=True, blank=True)
    meta_description  = models.TextField(max_length=500,null=True, blank=True)
    meta_keywords  = models.TextField(max_length=500,null=True, blank=True)
    canonical_tag  = models.TextField(max_length=500,null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name
    
class Tags(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,blank=True, null=True)

    class Meta:
        verbose_name = 'Tags'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tags, self).save(*args, **kwargs)
    
class Author(models.Model):
    name = models.CharField(max_length=200,null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to=rename_file, null=True)
    website = models.URLField(null=True)
    facebook = models.URLField(null=True)
    instagram = models.URLField(null=True)
    youtube = models.URLField(null=True)
    twitter = models.URLField(null=True)
    slug = models.SlugField(unique=True,blank=True, null=True)
    meta_title  = models.TextField(max_length=500,null=True, blank=True)
    meta_description  = models.TextField(max_length=500,null=True, blank=True)
    meta_keywords  = models.TextField(max_length=500,null=True, blank=True)
    canonical_tag  = models.TextField(max_length=500,null=True, blank=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Author'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Author, self).save(*args, **kwargs)


class Comments(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    comment = models.TextField()
    approve = models.BooleanField(default=False)
    date  = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
    def get_initials(self):
        parts = self.name.upper().split()
        if len(parts) == 1:
            return parts[0][:1]  
        else:
            return parts[0][:1] + ' ' + parts[-1][:1] 


class Blog(models.Model):
    category    = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    author      = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    title       = models.CharField(max_length=250,null=True)
    image_1     = models.ImageField(null=True,upload_to=rename_file)
    image_2     = models.ImageField(null=True,upload_to=rename_file)
    youtube_url = models.URLField(null=True)
    date        = models.DateField(auto_now_add=True,null=True)
    tags        = models.ManyToManyField(Tags, blank=True)
    slug        = models.SlugField( blank=True)
    quote       = models.TextField(blank=True, null=True)
    comments    = models.ManyToManyField(Comments, blank=True)
    short_description = models.TextField(null=True)
    full_description  = RichTextUploadingField(null=True)
    is_popular       = models.BooleanField(default=False)
    
    meta_title  = models.TextField(max_length=500,null=True, blank=True)
    meta_description  = models.TextField(max_length=500,null=True, blank=True)
    meta_keywords  = models.TextField(max_length=500,null=True, blank=True)
    canonical_tag  = models.TextField(max_length=500,null=True, blank=True)

    def countComments(self):
        return self.comments.filter(approve=True).count()

    def __str__(self):
        return self.title

class Translate(models.Model):
    language_options = (
    ('af', 'Afrikaans'), ('sq', 'Albanian'), ('am', 'Amharic'), ('ar', 'Arabic'), ('hy', 'Armenian'),
    ('as', 'Assamese'), ('ay', 'Aymara'), ('az', 'Azerbaijani'), ('bm', 'Bambara'), ('eu', 'Basque'),
    ('be', 'Belarusian'), ('bn', 'Bengali'), ('bho', 'Bhojpuri'), ('bs', 'Bosnian'), ('bg', 'Bulgarian'),
    ('ca', 'Catalan'), ('ceb', 'Cebuano'), ('ny', 'Chichewa'), ('zh-CN', 'Chinese (Simplified)'), ('zh-TW', 'Chinese (Traditional)'),
    ('co', 'Corsican'), ('hr', 'Croatian'), ('cs', 'Czech'), ('da', 'Danish'), ('dv', 'Dhivehi'),
    ('doi', 'Dogri'), ('nl', 'Dutch'), ('en', 'English'), ('eo', 'Esperanto'), ('et', 'Estonian'),
    ('ee', 'Ewe'), ('tl', 'Filipino'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'),
    ('gl', 'Galician'), ('ka', 'Georgian'), ('de', 'German'), ('el', 'Greek'), ('gn', 'Guarani'),
    ('gu', 'Gujarati'), ('ht', 'Haitian Creole'), ('ha', 'Hausa'), ('haw', 'Hawaiian'), ('iw', 'Hebrew'),
    ('hi', 'Hindi'), ('hmn', 'Hmong'), ('hu', 'Hungarian'), ('is', 'Icelandic'), ('ig', 'Igbo'),
    ('ilo', 'Ilocano'), ('id', 'Indonesian'), ('ga', 'Irish'), ('it', 'Italian'), ('ja', 'Japanese'),
    ('jw', 'Javanese'), ('kn', 'Kannada'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('rw', 'Kinyarwanda'),
    ('gom', 'Konkani'), ('ko', 'Korean'), ('kri', 'Krio'), ('ku', 'Kurdish (Kurmanji)'), ('ckb', 'Kurdish (Sorani)'),
    ('ky', 'Kyrgyz'), ('lo', 'Lao'), ('la', 'Latin'), ('lv', 'Latvian'), ('ln', 'Lingala'),
    ('lt', 'Lithuanian'), ('lg', 'Luganda'), ('lb', 'Luxembourgish'), ('mk', 'Macedonian'), ('mai', 'Maithili'),
    ('mg', 'Malagasy'), ('ms', 'Malay'), ('ml', 'Malayalam'), ('mt', 'Maltese'), ('mi', 'Maori'),
    ('mr', 'Marathi'), ('mni-Mtei', 'Meiteilon (Manipuri)'), ('lus', 'Mizo'), ('mn', 'Mongolian'), ('my', 'Myanmar (Burmese)'),
    ('ne', 'Nepali'), ('no', 'Norwegian'), ('or', 'Odia (Oriya)'), ('om', 'Oromo'), ('ps', 'Pashto'),
    ('fa', 'Persian'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pa', 'Punjabi'), ('qu', 'Quechua'),
    ('ro', 'Romanian'), ('ru', 'Russian'), ('sm', 'Samoan'), ('sa', 'Sanskrit'), ('gd', 'Scots Gaelic'),
    ('nso', 'Sepedi'), ('sr', 'Serbian'), ('st', 'Sesotho'), ('sn', 'Shona'), ('sd', 'Sindhi'),
    ('si', 'Sinhala'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('so', 'Somali'), ('es', 'Spanish'),
    ('su', 'Sundanese'), ('sw', 'Swahili'), ('sv', 'Swedish'), ('tg', 'Tajik'), ('ta', 'Tamil'),
    ('tt', 'Tatar'), ('te', 'Telugu'), ('th', 'Thai'), ('ti', 'Tigrinya'), ('ts', 'Tsonga'),
    ('tr', 'Turkish'), ('tk', 'Turkmen'), ('ak', 'Twi'), ('uk', 'Ukrainian'), ('ur', 'Urdu'),
    ('ug', 'Uyghur'), ('uz', 'Uzbek'), ('vi', 'Vietnamese'), ('cy', 'Welsh'), ('xh', 'Xhosa'),
    ('yi', 'Yiddish'), ('yo', 'Yoruba'), ('zu', 'Zulu')
    )
    language = models.CharField(max_length=50, choices=language_options)

    def __str__(self) -> str:
        return self.language
    
    # def get_name(self):
    #     for code, name in self.language_options:
    #         if self.language == code:
    #             return code, name
    #     return self.language, 'Unknown'


    