from rest_framework import generics, permissions
from .models import Block
from .serializers import BlockSerializer
from rest_framework.permissions import IsAuthenticated
from weshare_milestone_api.permissions import IsOwnerOrReadOnly


class BlockList(generics.ListCreateAPIView):
    """
    List all followers, i.e. all instances of a user
    following another user'.
    Create a follower, i.e. follow a user if logged in.
    Perform_create: associate the current logged in user with a follower.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BlockDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follower
    No Update view, as we either follow or unfollow users
    Destroy a follower, i.e. unfollow someone if owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
