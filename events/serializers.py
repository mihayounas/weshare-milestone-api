from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Event
        fields = ('id', 'title', 'start_time', 'end_time', 'location', 'description', 'created_at', 'updated_at')