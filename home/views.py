from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Article,Reviews
from .forms import ReviewForm
# import cloudinary.uploader

# Create your views here.

class ArticleList(generic.ListView):
    queryset =  Article.objects.all().order_by('title').values()
    template_name = 'home/index.html'
    paginate_by = 4

def detail(request, slug):
    
    queryset = Article.objects.all()
    detail = get_object_or_404(queryset, slug=slug)
    reviews = detail.chosen_article.all().order_by("-comment_date")
    reviews_count = detail.chosen_article.count()

    if request.method == "POST":    
        review_form = ReviewForm(data=request.POST)
        if review_form .is_valid():
            # post_image = review_form.cleaned_data['post_image']
            # result = cloudinary.uploader.upload(post_image)      
            review = review_form.save(commit=False)
            review.author = request.user
            review.article = detail 
            # reviews.post_image = UploadedImage()
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted Thank you!!'
            )            

    review_form = ReviewForm()
    
    return render(
        request,
        'home/detail.html',
        {
         'article':detail,
         'reviews':reviews,
         'reviews_count':reviews_count,
         'review_form': review_form,
        },
    )


class Reviews(generic.ListView):
    
    queryset = Reviews.objects.all()
    # model = Reviews
    # fields = '__all__'
    template_name = 'home/add_reviews.html'      
   
    def get_context_data(self, *args, **kwargs):
        article = super().get_context_data(*args, **kwargs)
        article['article_lists'] = Article.objects.all()           
        return article
             
        # def submit(self,request):       
        #     if  request.method == "POST":  
        #         review_form = ReviewForm(data=request.POST)
        #         if review_form.is_valid():
        #             review = review_form.save(commit=False)
        #             review.author = request.user
        #             review.article = detail 
        #             review.save()
        #     else:
        #         review_form = ReviewForm()

        #     return render(
        #          request,
        #         'home/add_review.html',            
        #         {
        #         'review_from':review_form,
        #     })

 
    

   

