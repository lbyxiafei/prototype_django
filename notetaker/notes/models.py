from django.db import models

class Bookmark(models.Model):
    name = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.title