from django.db import models
from authentication.models import User
# Create your models here.

class ClientTrainer(models.Model):
    client = models.ForeignKey(User, related_name='client', null=True,blank=True,on_delete=models.CASCADE)
    trainer = models.ForeignKey(User, related_name='trainer', null=True,blank=True,on_delete=models.CASCADE)
