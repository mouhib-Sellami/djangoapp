from django.db import models
from datetime import datetime
# Create your models here.

class User(models.Model):
    userId = models.IntegerField(primary_key=True,null=False)
    email = models.CharField(max_length=50,null=0)
    password = models.CharField(max_length=50,null=0)

class File(models.Model):
    fileId = models.AutoField(primary_key=1,null=False)
    userId = models.ForeignKey(User,on_delete=models.CASCADE,null = True,blank = True)

    file = models.FileField(blank=True,upload_to='cloudfiles')
    date = models.DateTimeField(max_length=50,default=datetime.now())

class Folder(models.Model):
    folderId = models.AutoField(primary_key=True,null=False)
    userId = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now())
    sharedUsers = models.ManyToManyField(User,related_name='users',null=True,blank= True)
    files = models.ManyToManyField(File,related_name='ffile',blank=True,null=True)

class Content(models.Model):
    contentId = models.AutoField(primary_key=1,null=0)
    folder = models.ForeignKey(Folder,on_delete=models.CASCADE,related_name='cfolder',null = True,blank= True)
    file = models.ForeignKey(File,on_delete=models.CASCADE,related_name='cfile',null=True,blank=True)

class cloud(models.Model):
    cloudId = models.AutoField(primary_key=True,null=0)
    userId = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    content = models.ForeignKey(Content,on_delete=models.CASCADE,null=True,blank=True,related_name='content')
