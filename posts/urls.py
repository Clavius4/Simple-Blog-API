from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.get_posts, name='get_posts'),
    path('posts/create/', views.create_post, name='create_posts'),
    path('posts/update/<int:pk>/', views.update_post, name='update_posts'),
    path('posts/delete/<int:pk>/', views.delete_post, name='delete_posts'),
]