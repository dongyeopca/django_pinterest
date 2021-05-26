from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=CASCADE,related_name='profile')
    image = models.ImageField(upload_to="profile/",null=True,blank=True)
    nickname= models.CharField(max_length=20,unique=True,null=True)
    message = models.CharField(max_length=100,null=True)
