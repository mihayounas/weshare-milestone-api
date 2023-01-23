from rest_framework import serializers
from .models import Event
from django.contrib.auth.models import User


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Event
        fields = ('owner', 'id', 'title', 'start_time', 'end_time', 'location', 'description', 'created_at', 'updated_at')

    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_authenticated:
            validated_data['owner'] = user
        return Event.objects.create(**validated_data)
