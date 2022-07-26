from django.http import Http404
from rest_framework import viewsets,status
from rest_framework.response import Response

from notes.models import Bookmark,Post,Tag
from .serializers import BookmarkSerializer,PostSerializer,TagSerializer

class BookmarkViewSet(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer 

    def get_queryset(self):
        bookmarks = Bookmark.objects.all()
        return bookmarks

    def create(self, request, *args, **kwargs):
        data = request.data
        new_bookmark = Bookmark.objects.create(
            title=data["title"], url=data['url'])
        new_bookmark.save()
        for tag in data["tags"]:
            tag_obj = Tag.objects.get_or_create(name=tag["name"])
            new_bookmark.tags.add(tag_obj[0])
        serializer = BookmarkSerializer(new_bookmark)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer 

    def get_queryset(self):
        posts = Post.objects.all()
        return posts

    def create(self, request, *args, **kwargs):
        data = request.data
        new_post = Post.objects.create(
            title=data["title"], content=data['content'])
        new_post.save()
        for tag in data["tags"]:
            tag_obj = Tag.objects.get_or_create(name=tag["name"])
            new_post.tags.add(tag_obj[0])
        serializer = PostSerializer(new_post)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer

    def get_queryset(self):
        tags = Tag.objects.all()
        return tags
    
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)