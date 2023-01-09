from django.urls import path
from shares import views

urlpatterns = [
    path('shares/', views.SharesList.as_view()),
    path('shares/<int:pk>/', views.SharesDetail.as_view()),
]
