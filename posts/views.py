from django.db.models import Count
from rest_framework import generics, permissions, filters
from weshare_milestone_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view


class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
        shares_count=Count('shares', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
        'shares_count',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(['POST'])
def share_post(request, id):
    post = get_object_or_404(Post, id=id)
    try:
        post.share()
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
        shares_count=Count('comment', distinct=True)
    ).order_by('-created_at')

