from rest_framework import serializers
from stories.models import Story


class StorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Story model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Story
        fields = ['id', 'created_at', 'owner', 'image', 'location',]
