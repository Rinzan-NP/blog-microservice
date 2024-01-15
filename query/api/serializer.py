from rest_framework.serializers import ModelSerializer
from . models import QueryPost,QueryComment

class CommentSerializer(ModelSerializer):
    class Meta:
        model = QueryComment
        fields = ['comment']

class PostWithCommentsSerializer(ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = QueryPost
        fields = ['id', 'title', 'comments']


class PostSerializer(ModelSerializer):
    class Meta:
        model = QueryPost
        fields = '__all__'

