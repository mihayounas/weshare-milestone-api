from rest_framework import generics, permissions
from weshare_milestone_api.permissions import IsOwnerOrReadOnly
from shares.models import Shares
from shares.serializers import SharesSerializer


class SharesList(generics.ListCreateAPIView):
    """
    List lof Shares or create a Share if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SharesSerializer
    queryset = Shares.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SharesDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SharesSerializer
    queryset = Shares.objects.all()
