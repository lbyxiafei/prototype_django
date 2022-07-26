from django.utils.encoding import smart_text
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from notes.models import Bookmark, Post, Tag

class CreatableSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            print(data)
            return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.slug_field, value=smart_text(data))
        except (TypeError, ValueError):
            self.fail('invalid')

class BookmarkSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many = True,
        queryset = Tag.objects.all(),
        slug_field = 'name'
    )

    class Meta:
        model = Bookmark
        fields = ('title', 'url', 'tags', 'pub_date')

    def create(self, validated_data):
        return Bookmark.objects.create(**validated_data) 

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'tag', 'pub_date')

    def create(self, validated_data):
        return Post.objects.create(**validated_data) 

class TagSerializer(serializers.ModelSerializer):
    # bookmarks = serializers.SlugRelatedField(
    #     many = True,
    #     queryset = Bookmark.objects.all(),
    #     slug_field = 'title'
    # )

    class Meta:
        model = Tag 
        fields = ('name', 'bookmarks', 'pub_date')

    def create(self, validated_data):
        return Tag.objects.create(**validated_data) 