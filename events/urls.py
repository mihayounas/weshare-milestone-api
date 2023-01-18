from django.urls import path
from .views import EventListCreateAPIView, EventDetailAPIView

urlpatterns = [
    path('events/', EventListCreateAPIView.as_view(), name='event_list_create'),
    path('events/<int:id>/', EventDetailAPIView.as_view(), name='event_detail'),
]