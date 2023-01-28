from rest_framework import serializers
from post_shares.models import PostShare


class PostShareSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    The create method handles the unique constraint on 'owner' and 'post'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = PostShare
        fields = ['id', 'created_at', 'owner', 'post']

    def create(self, validated_data):
        share, created = PostShare.objects.get_or_create(owner=validated_data['owner'], post=validated_data['post'])
        return share
