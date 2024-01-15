from django.urls import path
from .views import CommentView,EventView


urlpatterns = [
    path('comments/<id>', CommentView.as_view(), name='comments'),
    path('events/', EventView.as_view(), name='events'),

    
]
