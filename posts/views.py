from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer


# Get all posts
@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


# Create a new post
@api_view(['POST'])
def create_post(request):
    # The author is passed directly from the request, no authentication needed
    author = request.data.get('author', 'Unknown')  # Default to 'Unknown' if no author provided
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        # Save the post with the author field filled
        serializer.save(author=author)
        print("post created")
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Update an existing post
@api_view(['PUT'])
def update_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PostSerializer(post, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete a post
@api_view(['DELETE'])
def delete_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
