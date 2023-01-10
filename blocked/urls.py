from django.urls import path
from .views import BlockList, BlockDetail

urlpatterns = [
    path('blocks/', BlockList.as_view(), name='block-list'),
    path('blocks/<int:pk>/', BlockDetail.as_view(), name='block-detail'),
]
