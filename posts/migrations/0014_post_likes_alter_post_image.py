# Generated by Django 4.2.17 on 2025-01-23 15:16

import cloudinary.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0013_post_likes_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='default-post_e4kyej', max_length=255, null=True, verbose_name='image'),
        ),
    ]
