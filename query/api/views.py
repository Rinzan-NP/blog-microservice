from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import requests
from .serializer import PostWithCommentsSerializer
from .models import QueryPost

class GetPostsWithComments(APIView):
    def get(self, request, *args, **kwargs):
        posts = QueryPost.objects.all()
        serializer = PostWithCommentsSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        