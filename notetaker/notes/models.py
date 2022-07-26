from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Bookmark(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    tags = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    tags = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
