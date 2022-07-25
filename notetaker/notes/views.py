from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from notes.models import Bookmark,Tag
from notes.serializers import BookmarkSerializer

@api_view(['GET', 'POST', 'DELETE'])
def bookmarks(request):
    if request.method == 'GET':
        bookmarks = Bookmark.objects.all()
        bookmark = request.query_params.get('bookmark', None)
        if bookmark is not None:
            bookmarks = bookmarks.filter(bookmark__icontains=bookmark)
        bookmarks_serializer = BookmarkSerializer(bookmarks, many=True)
        return JsonResponse(bookmarks_serializer.data, safe=False)
    elif request.method == 'POST':
        bookmarks_data = JSONParser().parse(request)
        print(1)
        bmk = Bookmark(title=bookmarks_data['title'], url=bookmarks_data['url'])
        bmk.save()
        print(2)
        for tag_name in bookmarks_data['tags']:
            tg = Tag.objects.get_or_create(name=tag_name)
            print(tag_name)
            tg[0].save()
            print(3)
            bmk.tags.add(tg[0])
        print(4)
        bookmarks_serializer = BookmarkSerializer(bmk)
        print(bookmarks_serializer)
        return JsonResponse(bookmarks_serializer.data, status=status.HTTP_201_CREATED) 
    elif request.method == 'DELETE':
        count = Bookmark.objects.all().delete()
        return JsonResponse({'message': '{} Bookmarks were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
   