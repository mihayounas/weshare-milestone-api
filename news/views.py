from django.db.models import Count
from rest_framework import generics, permissions, filters
from weshare_milestone_api.permissions import IsOwnerOrReadOnly
from .models import News
from .serializers import NewsSerializer


class NewsList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = News.objects.all()


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = NewsSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = News.objects.all()
