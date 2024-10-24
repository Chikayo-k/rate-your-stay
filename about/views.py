from django.shortcuts import render
from .models import About

# Create your views here.


def about_us(request):
    """
    Renders the About page
    """
    about = About.objects.all().first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
