from django.shortcuts import render
from django.views import generic
from .models import Article
# Create your views here.

class ArticleList(generic.ListView):
    queryset =  Article.objects.all().order_by('title').values()
    template_name = 'home/index.html'
    paginate_by = 4