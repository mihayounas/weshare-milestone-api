from rest_framework import serializers
from .models import Event
from django.contrib.auth.models import User


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = Event
        fields = ('owner', 'id', 'title', 'start_time', 'end_time', 'location', 'description', 'created_at', 'updated_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
