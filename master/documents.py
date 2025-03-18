from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from blogs.models import Blog

@registry.register_document
class BlogDocument(Document):
    class Index:
        name = 'blog_index'  # Elasticsearch index ka naam
    
    class Django:
        model = Blog
        fields = [
            'title',
            'short_description',
            'meta_title',
            'meta_description',
            'meta_keywords',
        ]
