from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializer import PostSerializer
from rest_framework import status

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
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

        