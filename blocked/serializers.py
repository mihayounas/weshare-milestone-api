from rest_framework import serializers
from .models import Block
from django.contrib.humanize.templatetags.humanize import naturaltime


class BlockSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    blocked_name = serializers.ReadOnlyField(source='blocked.username')
    
    class Meta:
        model = Block
        fields = ('user', 'reason', 'duration', 'created_at', 'blocked_name')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
