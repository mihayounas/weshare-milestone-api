from rest_framework import generics
from .models import Block
from .serializers import BlockSerializer
from rest_framework.permissions import IsAuthenticated


class BlockList(generics.ListCreateAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
    permission_classes = [IsAuthenticated]


class BlockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
    permission_classes = [IsAuthenticated]
