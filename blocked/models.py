from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Block(models.Model):
    blocker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_blocker')
    blocked = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_blocked')
    reason = models.CharField(max_length=255)
    duration = models.DurationField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        duration_str = self.duration.__str__() if self.duration else ''
        reason_str = self.reason if self.reason else ''
        return f'Block for user {self.blocked.username} for reason: {reason_str} and duration: {duration_str}'
