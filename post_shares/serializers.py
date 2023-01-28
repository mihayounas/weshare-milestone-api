from rest_framework import serializers
from .models import PostShare


class PostShareSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = PostShare
        fields = ('id', 'owner', 'created_at')
        read_only_fields = ('id', 'created_at')