from rest_framework import serializers
from notes.models import Bookmark, Post, Tag, Tag2Bookmark, Tag2Post

class BookmarkSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Bookmark.objects.create(**validated_data) 

    class Meta:
        model = Bookmark
        fields = ('bookmark', 'url', 'pub_date')

class PostSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Post.objects.create(**validated_data) 

    class Meta:
        model = Post
        fields = ('post', 'content')

class TagSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Tag.objects.create(**validated_data) 

    class Meta:
        model = Tag 
        fields = ('tag', 'pub_date')

class Tag2BookmarkSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Tag2Bookmark.objects.create(**validated_data) 

    class Meta:
        model = Tag2Bookmark
        fields = ('tag', 'bookmark', 'is_linked', 'pub_date')

class Tag2PostSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Tag2Post.objects.create(**validated_data) 

    class Meta:
        model = Tag2Post
        fields = ('tag', 'post', 'is_linked', 'pub_date')