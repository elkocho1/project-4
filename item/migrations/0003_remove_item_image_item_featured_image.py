# Generated by Django 4.2.13 on 2024-07-10 16:37

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
        migrations.AddField(
            model_name='item',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placefolder', max_length=255, verbose_name='image'),
        ),
    ]
