# Generated by Django 4.2.19 on 2025-03-09 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_company_seo_socialmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_type', models.CharField(choices=[('Blogs', 'Blogs')], max_length=150, null=True)),
                ('show', models.BooleanField(default=True)),
            ],
        ),
    ]
