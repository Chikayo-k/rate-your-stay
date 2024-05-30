from . import views
from django.urls import path

urlpatterns = [   
    path('', views.ArticleList.as_view(), name='home'),
    path('reviews/', views.Reviews.as_view(), name='reviews'),
    path('<slug:slug>/', views.detail, name='detail'),  
    path('<slug:slug>/review_edit/<int:review_id>', views.review_edit, name='review_edit'),
]