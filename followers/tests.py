from django.test import TestCase
from django.contrib.auth.models import User
from .models import Follower


class FollowerModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='testuser1', password='testpass1'
        )
        self.user2 = User.objects.create_user(
            username='testuser2', password='testpass2'
        )

    def test_follower_creation(self):
        follower = Follower.objects.create(owner=self.user1, followed=self.user2)
        self.assertEqual(follower.owner, self.user1)
        self.assertEqual(follower.followed, self.user2)
        self.assertIsNotNone(follower.created_at)

    def test_duplicate_follower_creation(self):
        Follower.objects.create(owner=self.user1, followed=self.user2)
        with self.assertRaises(Exception):
            Follower.objects.create(owner=self.user1, followed=self.user2)

    def test_follower_ordering(self):
        follower1 = Follower.objects.create(owner=self.user1, followed=self.user2)
        follower2 = Follower.objects.create(owner=self.user2, followed=self.user1)
        followers = Follower.objects.all()
        self.assertEqual(list(followers), [follower2, follower1])

