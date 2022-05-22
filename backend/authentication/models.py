# from django.db import models
from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models

Goal_CHOICES = (
    (1, "Weight loss"),
    (2, "Weight gain"),
    (3, "Maintainance")
)
Exp_CHOICES = (
    (1, "Beginner"),
    (2, "Intermediate"),
    (3, "Advanced")
)
class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    age = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    goal = models.IntegerField(choices=Goal_CHOICES,null=True, default= 1)
    calories = models.IntegerField(null=True)
    gender = models.CharField(max_length=15,null=True)
    experience = models.IntegerField(choices=Exp_CHOICES, null=True, default=1)
    '''
    This is a custom version of the built in User class
    It contains all of the built in fields and functionality of the standard User
    You can add fields here for any additional properties you want a User to have
    This is useful for adding roles (Customer and Employee, for example)
    For just a few roles, adding boolean fields is advised
    '''
    # Example (note import of models above that is commented out)
    # this will add a column to the user table
    # is_student = models.BooleanField('student status', default=False)
