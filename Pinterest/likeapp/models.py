from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from articleapp.models import Article
# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(User,on_delete=CASCADE,related_name='like_record')
    article = models.ForeignKey(Article,on_delete=CASCADE,related_name='like_record')

    class Meta:
        unique_together=('user','article')
