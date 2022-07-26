from rest_framework import viewsets
from rest_framework.response import Response

from notes.models import Bookmark,Tag
from .serializers import BookmarkSerializer, TagSerializer

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


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer

    def get_queryset(self):
        tags = Tag.objects.all()
        return tags