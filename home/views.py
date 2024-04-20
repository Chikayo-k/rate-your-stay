from django.shortcuts import render
from django.views import generic
from .models import Article
# Create your views here.

class ArticleList(generic.ListView):
    queryset =  Article.objects.all()
    template_name = 'home/index.html'
    paginate_by = 4