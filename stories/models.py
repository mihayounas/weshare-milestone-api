from django.db import models
from django.contrib.auth.models import User


class Story(models.Model):
    """
    Follower model, related to 'owner' and 'followed'.
    """
    owner = models.ForeignKey(
        User, related_name='story', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', blank=False
    )
    location = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'image']

    def __str__(self):
        return f'{self.id} {self.image}'
