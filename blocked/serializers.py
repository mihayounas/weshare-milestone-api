from rest_framework import serializers
from .models import Block
from django.contrib.humanize.templatetags.humanize import naturaltime


class BlockSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    reason = serializers.ReadOnlyField(source='user.reason')
    duration = serializers.ReadOnlyField(source='user.duration')
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Block
        fields = ('user', 'reason', 'duration', 'created_at')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
