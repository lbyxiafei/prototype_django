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
    tag = serializers.SlugRelatedField(
        many = True,
        queryset = Tag.objects.all(),
        slug_field = 'name'
    )

    class Meta:
        model = Bookmark
        fields = ('title', 'url', 'tag', 'pub_date')

    def validate(self, data):
        return data

    def create(self, validated_data):
        print('?')
        # for tag in validated_data['tag']:
        #     Tag.objects.create(tag)
        print('??')
        for tag in validated_data['tag']:
            print(tag, type(tag), tag.name)
        print('???')
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