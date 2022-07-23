from django.db import models

class Bookmark(models.Model):
    bookmark = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.bookmark


class Post(models.Model):
    post = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.post

class Tag(models.Model):
    tag = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.tag

class Tag2Bookmark(models.Model):
    tag= models.ForeignKey(Tag, on_delete=models.CASCADE)
    bookmark= models.ForeignKey(Bookmark, on_delete=models.CASCADE)
    is_linked = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{str(self.tag)}-{str(self.bookmark)}"

class Tag2Post(models.Model):
    tag= models.ForeignKey(Tag, on_delete=models.CASCADE)
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    is_linked = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{str(self.tag)}-{str(self.post)}"
