from django.db import models


# Create your models here.
class Post(models.Model):
    userId = models.IntegerField()
    title = models.CharField(max_length=3000)
    body = models.TextField()

    def __str__(self):
        return self.title
