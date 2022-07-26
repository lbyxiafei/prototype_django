from rest_framework import serializers
from notes.models import Bookmark, Post, Tag

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('id', 'title', 'url', 'tags', 'pub_date')
        depth = 1

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'tags', 'pub_date')
        depth = 1

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag 
        fields = ('id', 'name', 'pub_date')