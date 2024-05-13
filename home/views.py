from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Article,Reviews

# Create your views here.

class ArticleList(generic.ListView):
    queryset =  Article.objects.all().order_by('title').values()
    template_name = 'home/index.html'
    paginate_by = 4

def detail(request, slug):
    
    queryset = Article.objects.all()
    detail = get_object_or_404(queryset, slug=slug)
    reviews = detail.chosen_article.all()
    

    return render(
        request,
        'home/detail.html',
        {
         'article':detail,
         'reviews':reviews,
        },
    )