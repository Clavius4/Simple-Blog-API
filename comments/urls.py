from django.urls import path

from comments import views
from comments.views import CommentsListCreate, CommentsListRetrieveUpdateDestroy

urlpatterns = [
    path('comments/', CommentsListCreate.as_view(), name='comments-list-create'),
    path('comments/<int:pk>/', CommentsListRetrieveUpdateDestroy.as_view(), name='comments-retrieve-update-destroy'),
]