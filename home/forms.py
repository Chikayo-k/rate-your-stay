from .models import Reviews, Article
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('comment_area',)