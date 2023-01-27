from rest_framework import serializers
from .models import Shares


class SharesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shares
        fields = ('id', 'post', 'owner', 'created_at')

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
