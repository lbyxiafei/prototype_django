from rest_framework import serializers
from notes.models import Bookmark, Post, Tag

class BookmarkSerializer(serializers.ModelSerializer):
    tag = serializers.SlugRelatedField(
        many = True,
        read_only = True,
        slug_field = 'name'
    )

    class Meta:
        model = Bookmark
        fields = ('title', 'url', 'tag', 'pub_date')

    def create(self, validated_data):
        return Bookmark.objects.create(**validated_data) 


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'tag', 'pub_date')

    def create(self, validated_data):
        return Post.objects.create(**validated_data) 

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag 
        fields = ('name', 'bookmark', 'pub_date')

    def create(self, validated_data):
        return Tag.objects.create(**validated_data) 