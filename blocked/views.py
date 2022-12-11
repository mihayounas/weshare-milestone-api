from rest_framework import generics, permissions
from weshare_milestone_api.permissions import IsOwnerOrReadOnly
from blocked.models import Blocked
from blocked.serializers import BlockedSerializer


class BlockedList(generics.ListCreateAPIView):
    """
    List lof Shares or create a Share if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BlockedSerializer
    queryset = Blocked.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BlockedDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BlockedSerializer
    queryset = Blocked.objects.all()
