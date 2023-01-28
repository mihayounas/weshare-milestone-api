from rest_framework import serializers
from post_shares.models import PostShare


class PostShareSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = PostShare
        fields = ('owner', 'post')

    def create(self, validated_data):
        owner = validated_data.get('owner')
        post = validated_data.get('post')
        post_share = PostShare.objects.create(owner=owner, post=post)
        return post_share