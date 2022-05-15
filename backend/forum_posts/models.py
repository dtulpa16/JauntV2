from django.db import models
from authentication.models import User

# Create your models here.
class ForumPost(models.Model):
    user = models.ForeignKey(User, null=True,blank=True,on_delete=models.CASCADE)
    body = models.CharField(max_length=1000,null=True)
    likes = models.IntegerField(null=True, default = 0)

class ForumReply(models.Model):
    post = models.ForeignKey(ForumPost, null=True,blank=True,on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True,blank=True,on_delete=models.CASCADE)
    body = models.CharField(max_length=1000,null=True)
    likes = models.IntegerField(null=True, default = 0)