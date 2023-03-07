from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime
from .models import Event


class EventTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.event = Event.objects.create(
            owner=self.user,
            title='Test Event',
            start_time=datetime.now(),
            end_time=datetime.now(),
            location='Test Location',
            description='Test Description',
        )

    def test_event_saved_correctly(self):
        saved_event = Event.objects.get(pk=self.event.id)
        self.assertEqual(saved_event.owner, self.user)
        self.assertEqual(saved_event.title, 'Test Event')
        self.assertEqual(saved_event.location, 'Test Location')
        self.assertEqual(saved_event.description, 'Test Description')

    def test_is_owner_method(self):
        other_user = User.objects.create_user(username='otheruser', password='otherpass')
        self.assertTrue(self.event.is_owner(self.user))
        self.assertFalse(self.event.is_owner(other_user))
