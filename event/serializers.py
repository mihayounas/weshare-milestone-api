from rest_framework import serializers
from .models import Event
from django.contrib.auth.models import User


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created_at = serializers.ReadOnlyField()
    delete_url = serializers.HyperlinkedIdentityField(
        view_name='events:delete-event',
        lookup_field='pk'
    )

    class Meta:
        model = Event
        fields = ('owner', 'id', 'title', 'start_time', 'end_time', 'location', 'description', 'created_at', 'updated_at', 'delete_url')

