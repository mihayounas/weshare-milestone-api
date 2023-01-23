from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_owner(self, user):
        return self.owner == user

    def __str__(self):
        return f'{self.id} {self.title}'
