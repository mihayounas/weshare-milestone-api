from rest_framework import generics, permissions
from weshare_milestone_api.permissions import IsOwnerOrReadOnly
from post_shares.models import PostShare
from post_shares.serializers import PostShareSerializer



class PostSharesList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = PostShare.objects.all()
    serializer_class = PostShareSerializer



class PostSharesDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostShareSerializer
    queryset = PostShare.objects.all()
