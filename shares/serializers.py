from rest_framework import serializers
from .models import Shares


class SharesSerializer(serializers.ModelSerializer):
    
    owner = serializers.ReadOnlyField(source='owner.username')

    
    class Meta:
        model = Shares
        fields = ('id', 'post', 'owner', 'created_at')

    def create(self, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            validated_data["owner"] = request.user
        return super().create(validated_data)