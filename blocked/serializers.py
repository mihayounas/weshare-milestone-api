from rest_framework import serializers
from blocked.models import Blocked


class BlockedSerializer(serializers.ModelSerializer):
    """
    Serializer for the Shares model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    users = serializers.ReadOnlyField(source='users.username')

    class Meta:
        model = Blocked
        fields = ['id', 'owner', 'users']
