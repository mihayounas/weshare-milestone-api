from rest_framework import serializers
from .models import PostShare

class PostShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostShare
        fields = ('id', 'owner', 'post', 'created_at')
        read_only_fields = ('id', 'created_at')