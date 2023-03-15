from rest_framework import generics
from .models import Event
from .serializers import EventSerializer
from django.shortcuts import HttpResponse
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, permissions


class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(owner=self.request.user)
        else:
            return HttpResponse(status=401)


class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def update(self, request, *args, **kwargs):
        event = self.get_object()
        if not event.is_owner(request.user):
            raise PermissionDenied("You do not have permission to edit this event.")
        return super().update(request, *args, **kwargs)

    def perform_destroy(self, instance):
        if not instance.is_owner(self.request.user):
            raise PermissionDenied("You do not have permission to delete this event.")
        instance.delete()
        

class DeleteEventAPIView(generics.DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        event = self.get_object()
        if not event.is_owner(request.user):
            raise PermissionDenied("You do not have permission to delete this event.")
        return super().delete(request, *args, **kwargs)