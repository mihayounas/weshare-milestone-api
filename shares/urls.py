from django.urls import path
from shares import views

urlpatterns = [
    path('shared/', views.SharesList.as_view()),
    path('shared/<int:pk>/', views.SharesDetail.as_view()),
]
