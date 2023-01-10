from rest_framework import serializers
from blocked.models import Block


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ('user', 'reason', 'duration')
