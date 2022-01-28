from django.db import models

class crdata(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    fee=models.FloatField()
    sub1=models.CharField(max_length=100)
    sub2=models.CharField(max_length=100)
    sub3=models.CharField(max_length=100)
    sub4=models.CharField(max_length=100)

