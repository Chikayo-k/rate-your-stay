# Generated by Django 4.2.11 on 2024-05-27 09:36

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_article_article_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='post_image',
            field=cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, verbose_name='Posted image'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='rate',
            field=models.IntegerField(choices=[(0, 'Rate your stay'), (1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], default=0),
        ),
    ]
