from django.db import models
from authentication.models import User

Rating_CHOICES = (
    (1, 'Poor'),
    (2, 'Average'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent')
)

# Create your models here.
class TrainerReview(models.Model):
    user = models.ForeignKey(User, null=True,blank=True,on_delete=models.CASCADE)
    body = models.CharField(max_length=1000,null=True)
    rating = models.IntegerField(choices=Rating_CHOICES, default=1)