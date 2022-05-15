from django.db import models
from authentication.models import User

# Create your models here.
class TrainerBlog(models.Model):
    user = models.ForeignKey(User, null=True,blank=True,on_delete=models.CASCADE)
    body = models.CharField(max_length=1000,null=True)
    likes = models.IntegerField(default=0, null = True)