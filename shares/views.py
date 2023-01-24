from rest_framework import generics, permissions
from weshare_milestone_api.permissions import IsOwnerOrReadOnly
from shares.models import Shares
from shares.serializers import ShareSerializer


class SharesList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ShareSerializer
    queryset = Shares.objects.all()

    def post(self, request, format=None):
        serializer = ShareSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SharesDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ShareSerializer
    queryset = Shares.objects.all()



    
