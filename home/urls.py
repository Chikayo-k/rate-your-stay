from . import views
from django.urls import path

urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('<slug:slug>/', views.detail, name='detail'),
    path('<slug:slug>/edit_review/<int:review_id>', views.review_edit, name='review_edit'),  # noqa
    path('<slug:slug>/review_delete/<int:review_id>', views.review_delete, name='review_delete'),  # noqa
]
