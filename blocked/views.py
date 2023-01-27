from rest_framework import generics, permissions
from .models import Block
from .serializers import BlockSerializer
from rest_framework.permissions import IsAuthenticated
from weshare_milestone_api.permissions import IsOwnerOrReadOnly


class BlockList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BlockSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Block.objects.filter(blocker=user)
        return queryset


class BlockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
    permission_classes = [IsOwnerOrReadOnly]
