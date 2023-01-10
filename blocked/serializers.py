from django.shortcuts import get_object_or_404
from rest_framework import serializers, views, permissions, status
from rest_framework.response import Response
from django.utils import timezone
from blocked.models import Block


# Serializers
class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['user', 'reason', 'duration', 'created_at']
