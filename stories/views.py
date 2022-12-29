from django.db.models import Count
from rest_framework import generics, permissions, filters
from weshare_milestone_api.permissions import IsOwnerOrReadOnly
from .models import Story
from .serializers import StorySerializer


class StoryList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Story.objects.annotate(
        stories_count=Count('owner__story', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'content',
        'location',
    ]
    ordering_fields = [
        'owner__username',
        'content',
        'story_count',
        'location',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a story and edit or delete it if you own it.
    """
    serializer_class = StorySerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Story.objects.annotate(
        story_count=Count('owner__story', distinct=True)
    ).order_by('-created_at')
