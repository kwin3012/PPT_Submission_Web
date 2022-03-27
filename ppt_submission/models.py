from imp import cache_from_source
from tabnanny import check
from django.db import models
from django.forms import CharField

# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(max_length=100) 

class Student(models.Model):
    t = models.ForeignKey(Topic,default=1,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=False)
    email = models.EmailField(max_length=100,unique=True,blank=False,null=True)
    roll = models.IntegerField(blank=False,error_messages={'unique':"you have already selected a topic!"})
    ppt_submitted = models.BooleanField(default=False)

class File(models.Model):
    tt = models.ForeignKey(Student,default=1,on_delete=models.CASCADE)
    roll_check = models.IntegerField(blank=False,null=True)
    file = models.FileField(upload_to="",blank=False)           














































