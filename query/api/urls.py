from django.urls import path
from .views import GetPostsWithComments,EventView

urlpatterns = [
    path('posts/', GetPostsWithComments.as_view(), name="post_with_comment"),
    path('events/', EventView.as_view(), name="event")
]
