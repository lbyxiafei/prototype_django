from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.tag

class Bookmark(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    tag = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
