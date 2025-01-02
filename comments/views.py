from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from comments.models import Comments
from comments.serializers import CommentSerializer


# Create your views here.
# Class-Based Views

# Listing and Creating
class CommentsListCreate(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save()


# Retrieving, Updating, and Destroying
class CommentsListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        serializer.save()


    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comments.DoesNotExist:
            return Response(f'Comment not found', status=status.HTTP_404_NOT_FOUND)

    def perform_destroy(self, instance):
        instance.delete()

