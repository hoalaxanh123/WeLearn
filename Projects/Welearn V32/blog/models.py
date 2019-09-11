from django.db import models

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=100)
    shortName = models.CharField(max_length=50)
    description = models.TextField()
    dateCreate = models.DateTimeField(auto_now_add=True)
    thumbail = models.CharField(max_length=100,default='')
    logo = models.CharField(max_length=100,default='')

class Log(models.Model):
    title = models.CharField( max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    title = models.CharField(max_length= 100)
    subjectID = models.IntegerField()
    description = models.TextField()

class Post(models.Model):
    catID = models.IntegerField('Category ID')
    title = models.CharField(max_length=500)
    description = models.TextField('Description ')
    content = models.TextField('Content ')
    dateCreate = models.DateTimeField(auto_now_add=True)
    creator = models.CharField(max_length=100)
    viewCount = models.IntegerField("View count " , default='0', editable=False)

class FeedBack(models.Model):
    creator = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    content = models.TextField()

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=500)
    realname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    role = models.IntegerField()



