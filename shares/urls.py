from django.urls import path
from shares import views

urlpatterns = [
    path('posts/${id}/shared', views.SharesList.as_view()),
    path('posts/${id}/shared/<int:pk>/', views.SharesDetail.as_view()),
]
