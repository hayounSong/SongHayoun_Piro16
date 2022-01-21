from tkinter import CASCADE
from django.db import models

# Create your models here.


class Devtool(models.Model):

    title=models.CharField(max_length=100)
    kind=models.CharField(max_length=100)
    content=models.TextField()
    def __str__(self):
        return self.title
    
class Idea(models.Model):

    choice_devtool=(('javascript','javascript'),('Python','Python'))

    title=models.CharField(max_length=100)
    image=models.ImageField(null=True,blank=True)
    content=models.TextField()
    like=models.IntegerField()
    devtool=models.ForeignKey(Devtool,on_delete=models.CASCADE)
    def __str__(self):
        return self.title