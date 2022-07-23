from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from notes.models import Bookmark
from notes.serializers import BookmarkSerializer

@api_view(['GET', 'POST'])
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
        bookmarks_serializer = BookmarkSerializer(data=bookmarks_data)
        if bookmarks_serializer.is_valid():
            bookmarks_serializer.save()
            return JsonResponse(bookmarks_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(bookmarks_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   