from django.urls import path
from .views import CommentView


urlpatterns = [
    path('comments/<id>', CommentView.as_view(), name='comments'),

    
]
