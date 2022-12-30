from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Shares(models.Model):
    """
    Shares model, related to 'owner' and 'post'.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='shares', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post} {self.id}'

