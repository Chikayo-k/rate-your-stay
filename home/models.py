from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES=(0,'Beach'),(1,'History'),(3,'City')
STATUS=(0,'Draft'),(0,'Published')
RATE=(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)

class Article(models.Model):
    title = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=0)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f'Article Name: {self.title}'


class Reviews(models.Model):
    article_id=models.ForeignKey
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='chosen_articl')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    review_title = models.CharField(max_length=20)
    rate = models.IntegerField(choices=RATE, default=0)
    comment_area = models.TextField()
    comment_date = models.DateTimeField(auto_now_add= True)

    class Meta:
        ordering = ['-comment_date']
    
    def __str__(self):
        return f'Comment for : {self.article}'
