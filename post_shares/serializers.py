from rest_framework import serializers
from .models import PostShare


class PostShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostShare
        fields = ('id', 'owner', 'post', 'created_at')
        read_only_fields = ('id', 'created_at')

    def create(self, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            validated_data["owner"] = request.user
        return super().create(validated_data)