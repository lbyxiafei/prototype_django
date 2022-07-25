from django.contrib import admin
from notes.models import Bookmark, Post, Tag

admin.site.register(Bookmark)
admin.site.register(Post)
admin.site.register(Tag)