from rest_framework import status
from .serializer import CommentSerializer
from .models import Comments
from rest_framework.response import Response
from rest_framework.views import APIView
import json
import requests


class CommentView(APIView):
    def get(self, request, id):
        comments = Comments.objects.filter(post_id=id)
        serializer = CommentSerializer(comments, many=True)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request, id):
        data = request.data
        serializer = CommentSerializer(data=data)

        

        if serializer.is_valid():
            serializer.save()
            url = "http://127.0.0.1:8005/events/"
            params = {"type": "comment_created", "data": serializer.data}
            headers = {"Content-Type": "application/json"}
            requests.post(url=url, data=json.dumps(params), headers=headers)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class EventView(APIView):
    def post(self, request):
        message = "Event received"
        return Response(message)
