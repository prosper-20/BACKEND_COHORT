from .serializers import PostSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .models import Post
from rest_framework.views import APIView

class ListAllPostsView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ListAllPostsView(APIView):
    def get(self, request):
        all_posts = Post.objects.all()

