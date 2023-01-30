from django.urls import path
from .views import EventListCreateAPIView, EventDetailAPIView

urlpatterns = [
    path('event/', EventListCreateAPIView.as_view(), name='event_list_create'),
    path('event/<int:pk>/', EventDetailAPIView.as_view(), name='event_detail'),
]
