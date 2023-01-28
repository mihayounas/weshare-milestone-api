from django.urls import path
from post_shares import views

urlpatterns = [
    path('share/', views.PostSharesList.as_view()),
    path('share/<int:pk>/', views.PostSharesDetail.as_view()),
]