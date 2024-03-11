# Generated by Django 5.0.2 on 2024-02-24 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=None, max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='food',
            name='slug',
            field=models.SlugField(default=None, max_length=100, unique=True),
        ),
    ]
