from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import requests
from .serializer import PostWithCommentsSerializer,PostSerializer
from .models import QueryPost,QueryComment

class GetPostsWithComments(APIView):
    def get(self, request, *args, **kwargs):
        posts = QueryPost.objects.all()
        serializer = PostWithCommentsSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class EventView(APIView):
    def post(self, request):
        data = request.data
        #{'type': 'post_created', 'data': {'id': 37, 'title': 'fsdf'}}
        
        if data['type'] == 'post_created':
            serializer = PostSerializer(data=data['data'])
            if serializer.is_valid():
                serializer.save()
        
        elif data['type'] == 'comment_created':
            comment_data = data['data']
            post_id = comment_data.get('post_id')
            comment_text = comment_data.get('comment')
            post_instance = QueryPost.objects.get(id=post_id)
            comment_instance = QueryComment(post=post_instance, comment=comment_text)
            comment_instance.save()

            return Response({'message': 'Comment created successfully'}, status=status.HTTP_201_CREATED)

        
        return Response( status=status.HTTP_200_OK)

