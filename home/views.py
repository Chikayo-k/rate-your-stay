from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Article, Reviews
from .forms import ReviewForm

# import cloudinary.uploader

# Create your views here.


class ArticleList(generic.ListView):
    queryset = Article.objects.all().order_by("title").values()
    template_name = "home/index.html"
    paginate_by = 4


def detail(request, slug):
    """
    Display an individual article
    """
    queryset = Article.objects.all()
    detail = get_object_or_404(queryset, slug=slug)
    reviews = detail.chosen_article.all().order_by("-comment_date")
    reviews_count = detail.chosen_article.count()
    # Write Review Submission
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.article = detail
            review.save()
            messages.add_message(
                request, messages.SUCCESS, "Comment submitted Thank you!!"
            )

    review_form = ReviewForm()

    return render(
        request,
        "home/detail.html",
        {
            "article": detail,
            "reviews": reviews,
            "reviews_count": reviews_count,
            "review_form": review_form,
        },
    )


def review_edit(request, slug, review_id):
    """
    view to edit review
    """
    if request.method == "POST":

        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Reviews, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.post = Reviews
            review.approverd = False
            review.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(request, messages.ERROR, "Error Comment Updating")  # noqa

        return HttpResponseRedirect(reverse("detail", args=[slug]))


def review_delete(request, slug, review_id):
    """
    view to delete review
    """
    queryset = Article.objects.filter(status=1)
    article = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Reviews, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, "Review deleted!")
    else:
        messages.add_message(request, messages.ERROR, "Not Success!")

    return HttpResponseRedirect(reverse("detail", args=[slug]))
