from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Create your models here.

CATEGORY_CHOICES = (0, "Beach"), (1, "History"), (2, "City")
STATUS = (0, "Draft"), (1, "Published")
RATE = (0, "Rate your stay"), (1, "★"), (2, "★★"), (3, "★★★"), (4, "★★★★"), (5, "★★★★★")  # noqa


class Article(models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=0)
    description = models.TextField(null=True)
    content = models.TextField()
    article_image = CloudinaryField('cover image', default='placeholder')
    detail_image = CloudinaryField('detail image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f'Article Name: {self.title}'


class Reviews(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='chosen_article')  # noqa
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')  # noqa
    review_title = models.CharField(max_length=20)
    rate = models.IntegerField(choices=RATE, default=0)
    comment_area = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    post_image = CloudinaryField('Post image', blank=True, null=True)

    class Meta:
        ordering = ['-comment_date']

    def __str__(self):
        return f'Comment for : {self.article}'
