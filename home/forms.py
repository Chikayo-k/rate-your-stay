from .models import Reviews
from .models import Reviews as Reviews, Article
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['review_title','rate','comment_area']