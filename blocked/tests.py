from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from .models import Block


class BlockModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.block = Block.objects.create(user=self.user, reason='Testing', duration=timedelta(minutes=30))

    def test_block_created_at(self):
        self.assertIsInstance(self.block.created_at, timezone.datetime)
        
    def test_block_duration(self):
        self.assertIsInstance(self.block.duration, timedelta)

    def test_block_string_representation(self):
        self.assertEqual(str(self.block), 'Block for user testuser for reason: Testing and duration: 30:00:00')
    
    def test_block_user(self):
        self.assertEqual(self.block.user, self.user)
        
    def test_block_reason(self):
        self.assertEqual(self.block.reason, 'Testing')
        
    def test_block_duration_is_null(self):
        block_without_duration = Block.objects.create(user=self.user, reason='Testing')
        self.assertEqual(block_without_duration.duration, None)