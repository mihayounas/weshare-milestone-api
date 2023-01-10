from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from blocked.models import Block
from .serializers import BlockSerializer
from rest_framework.response import Response
from rest_framework import status


class BlockList(generics.CreateAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlockDetail(generics.RetrieveUpdateAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        block = self.get_object()
        block.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
