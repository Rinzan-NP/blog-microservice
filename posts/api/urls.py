from django.urls import path
from .views import PostView,EventView

urlpatterns = [
    path('posts/create/', PostView.as_view(), name="posts"),
    path('events/',EventView.as_view(), name="events")
]
