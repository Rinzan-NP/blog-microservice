from django.urls import path
from .views import GetPostsWithComments

urlpatterns = [
    path('posts/', GetPostsWithComments.as_view(), name="post_with_comment")
]
