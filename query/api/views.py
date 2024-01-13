from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializer import PostSerializer
from rest_framework import status
import requests

class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        serialized_data = serializer.data
        return Response(serialized_data)
    
    def post (self, request):
        data = request.data 
        serializer = PostSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            url = "http://127.0.0.1:8005/events/"
            parames = {
                "type": "post_created",
                "data": serializer.data
            }
            r = requests.post(url=url, data = parames)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

        