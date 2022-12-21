from rest_framework import serializers

from shares.models import Shares


class SharesSerializer(serializers.ModelSerializer):
    """
    Serializer for the Shares model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Shares
        fields = ['id', 'created_at', 'owner', 'post']