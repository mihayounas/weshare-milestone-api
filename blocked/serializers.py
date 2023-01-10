from django.shortcuts import get_object_or_404
from rest_framework import serializers
from blocked.models import Block


# Serializers
class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['user', 'reason', 'duration']
