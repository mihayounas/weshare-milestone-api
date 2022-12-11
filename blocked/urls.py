from django.urls import path
from blocked import views

urlpatterns = [
    path('blocked/', views.BlockedList.as_view()),
    path('blocked/<int:pk>/', views.BlockedDetail.as_view()),
]