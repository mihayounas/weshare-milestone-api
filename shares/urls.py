from django.urls import path
from shares import views

urlpatterns = [
    path('posts/shares/', views.SharesList.as_view()),
    path('posts/<int:pk>/shares/', views.SharesDetail.as_view()),
]