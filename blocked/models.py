from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Block(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
    duration = models.DurationField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.duration
