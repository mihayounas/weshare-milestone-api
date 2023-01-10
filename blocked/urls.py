from django.urls import path
from blocked import views

urlpatterns = [
    path('blocked/', views.BlockList.as_view(), name='block-list'),
    path('blocked/<int:pk>/', views.BlockDetail.as_view(), name='block-detail'),
]
