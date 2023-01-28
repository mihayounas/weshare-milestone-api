from rest_framework import serializers
from .models import Shares


class SharesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shares
        fields = ('id', 'post', 'owner', 'created_at')