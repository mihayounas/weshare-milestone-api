from rest_framework import serializers

from shares.models import Shares


class SharesSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    The create method handles the unique constraint on 'owner' and 'post'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Shares
        fields = ['id', 'created_at', 'owner', 'post']
