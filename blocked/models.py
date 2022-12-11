from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from profiles.models import Profile
from posts.models import Post


class Blocked(models.Model):
    """
    Blocked model, related to 'owners'.
    """
    owner = models.ForeignKey(
        User, related_name='blocked_users', on_delete=models.CASCADE
    )
    users = models.ManyToManyField(User, related_name="blocked_by")

    def ignore_users(self):
        blocked_users = User.objects.get(username=X).blocked_users.users.all()
        return Post.objects.filter(~Q(author__in=blocked_users))

    def __str__(self):
        return f'{self.owner} {self.users}'
