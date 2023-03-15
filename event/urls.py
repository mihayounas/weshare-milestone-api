from django.urls import path
from .views import EventListCreateAPIView, EventDetailAPIView, DeleteEventAPIView

app_name = 'events'

urlpatterns = [
    path('event/', EventListCreateAPIView.as_view(), name='event-list-create'),
    path('event/<int:pk>/', EventDetailAPIView.as_view(), name='event-detail'),
    path('event/<int:pk>/delete/', DeleteEventAPIView.as_view(), name='delete-event'),
]

