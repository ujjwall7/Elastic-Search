# Generated by Django 4.2.19 on 2025-03-09 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projects_projectsimages_seo_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SEO',
        ),
        migrations.AddField(
            model_name='category',
            name='canonical_tag',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_keywords',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_title',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='canonical_tag',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='meta_description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='meta_keywords',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='meta_title',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
