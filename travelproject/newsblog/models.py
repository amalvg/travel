from django.db import models

# Create your models here.
class blog(models.Model):
    head=models.CharField(max_length=100)
    img=models.ImageField(upload_to='news')
    desc=models.TextField()
    date=models.DateField()