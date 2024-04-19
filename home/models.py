from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

CATEGORY_CHOICES=(0,'Beach'),(1,'History'),(3,'City')
STATUS=(0,'Draft'),(0,'Published')

class Article(models.Model):
    title = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=0)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    
