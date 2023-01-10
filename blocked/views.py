from rest_framework import generics, permissions
from .models import Block
from .serializers import BlockSerializer
from rest_framework.permissions import IsAuthenticated
from weshare_milestone_api.permissions import IsOwnerOrReadOnly


class BlockList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BlockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
    permission_classes = [IsOwnerOrReadOnly]
