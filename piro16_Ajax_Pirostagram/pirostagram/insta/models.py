from django.db import models

# Create your models here.
class Post(models.Model):
    
    content=models.TextField()
    like=models.IntegerField()

class Comment(models.Model):

    content=models.TextField()
    like=models.IntegerField()
    post=models.ForeignKey(Post, on_delete=models.CASCADE)