from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pictures')
    desc=models.TextField()
    price=models.IntegerField(default=0)
    offer=models.BooleanField(default=False)

class special(models.Model):
    name1=models.CharField(max_length=100)
    img1=models.ImageField(upload_to='spcl')
    desc1=models.TextField()
    price1=models.IntegerField(default=0)

class news(models.Model):
    head=models.CharField(max_length=100)
    img=models.ImageField(upload_to='news')
    desc=models.TextField()
    date=models.DateField()