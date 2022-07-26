from django.utils.encoding import smart_text
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from notes.models import Bookmark, Post, Tag

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('title', 'url', 'tags', 'pub_date')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'tags', 'pub_date')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag 
        fields = ('name', 'pub_date')