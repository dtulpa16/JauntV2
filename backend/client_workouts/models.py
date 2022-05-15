from django.db import models
from authentication.models import User
Frequency_CHOICES = (
    (1, '1 Day Per Week'),
    (2, '2 Day Per Week'),
    (3, '3 Day Per Week'),
    (4, '4 Day Per Week'),
    (5, '5 Day Per Week'),
    (5, '6 Day Per Week'),
    (5, '7 Day Per Week'),
)
# Create your models here.
class Workout(models.Model):
    user = models.ForeignKey(User,blank=True, null=True,on_delete=models.CASCADE)
    notes = models.CharField(max_length=1000,null=True,blank=True, default = 'No Notes')
    days_per_week = models.IntegerField(choices=Frequency_CHOICES, default=1)
    #day1
    day1ex1 = models.CharField(max_length=50,null=True)
    day1ex1sets = models.IntegerField(null=0)
    day1ex1reps = models.IntegerField(null=0)
    day1ex2 = models.CharField(max_length=50,null=True)
    day1ex2reps = models.IntegerField(null=0)
    day1ex2sets = models.IntegerField(null=0)
    day1ex3 = models.CharField(max_length=50,null=True)
    day1ex3sets = models.IntegerField(null=0)
    day1ex3reps = models.IntegerField(null=0)
    day1ex4 = models.CharField(max_length=50,null=True)
    day1ex4sets = models.IntegerField(null=0)
    day1ex4reps = models.IntegerField(null=0)
    #day2
    day2ex1 = models.CharField(max_length=50,null=True)
    day2ex1sets = models.IntegerField(null=0)
    day2ex1reps = models.IntegerField(null=0)
    day2ex2 = models.CharField(max_length=50,null=True)
    day2ex2reps = models.IntegerField(null=0)
    day2ex2sets = models.IntegerField(null=0)
    day2ex3 = models.CharField(max_length=50,null=True)
    day2ex3sets = models.IntegerField(null=0)
    day2ex3reps = models.IntegerField(null=0)
    day2ex4 = models.CharField(max_length=50,null=True)
    day2ex4sets = models.IntegerField(null=0)
    day2ex4reps = models.IntegerField(null=0)
    #day3
    day3ex1 = models.CharField(max_length=50,null=True)
    day3ex1sets = models.IntegerField(null=0)
    day3ex1reps = models.IntegerField(null=0)
    day3ex2 = models.CharField(max_length=50,null=True)
    day3ex2reps = models.IntegerField(null=0)
    day3ex2sets = models.IntegerField(null=0)
    day3ex3 = models.CharField(max_length=50,null=True)
    day3ex3sets = models.IntegerField(null=0)
    day3ex3reps = models.IntegerField(null=0)
    day3ex4 = models.CharField(max_length=50,null=True)
    day3ex4sets = models.IntegerField(null=0)
    day3ex4reps = models.IntegerField(null=0)
    #day4
    day4ex1 = models.CharField(max_length=50,null=True)
    day4ex1sets = models.IntegerField(null=0)
    day4ex1reps = models.IntegerField(null=0)
    day4ex2 = models.CharField(max_length=50,null=True)
    day4ex2reps = models.IntegerField(null=0)
    day4ex2sets = models.IntegerField(null=0)
    day4ex3 = models.CharField(max_length=50,null=True)
    day4ex3sets = models.IntegerField(null=0)
    day4ex3reps = models.IntegerField(null=0)
    day4ex4 = models.CharField(max_length=50,null=True)
    day4ex4sets = models.IntegerField(null=0)
    day4ex4reps = models.IntegerField(null=0)
    #day5
    day5ex1 = models.CharField(max_length=50,null=True)
    day5ex1sets = models.IntegerField(null=0)
    day5ex1reps = models.IntegerField(null=0)
    day5ex2 = models.CharField(max_length=50,null=True)
    day5ex2reps = models.IntegerField(null=0)
    day5ex2sets = models.IntegerField(null=0)
    day5ex3 = models.CharField(max_length=50,null=True)
    day5ex3sets = models.IntegerField(null=0)
    day5ex3reps = models.IntegerField(null=0)
    day5ex4 = models.CharField(max_length=50,null=True)
    day5ex4sets = models.IntegerField(null=0)
    day5ex4reps = models.IntegerField(null=0)
    #day6
    day6ex1 = models.CharField(max_length=50,null=True)
    day6ex1sets = models.IntegerField(null=0)
    day6ex1reps = models.IntegerField(null=0)
    day6ex2 = models.CharField(max_length=50,null=True)
    day6ex2reps = models.IntegerField(null=0)
    day6ex2sets = models.IntegerField(null=0)
    day6ex3 = models.CharField(max_length=50,null=True)
    day6ex3sets = models.IntegerField(null=0)
    day6ex3reps = models.IntegerField(null=0)
    day6ex4 = models.CharField(max_length=50,null=True)
    day6ex4sets = models.IntegerField(null=0)
    day6ex4reps = models.IntegerField(null=0)
    #day7
    day7ex1 = models.CharField(max_length=50,null=True)
    day7ex1sets = models.IntegerField(null=0)
    day7ex1reps = models.IntegerField(null=0)
    day7ex2 = models.CharField(max_length=50,null=True)
    day7ex2reps = models.IntegerField(null=0)
    day7ex2sets = models.IntegerField(null=0)
    day7ex3 = models.CharField(max_length=50,null=True)
    day7ex3sets = models.IntegerField(null=0)
    day7ex3reps = models.IntegerField(null=0)
    day7ex4 = models.CharField(max_length=50,null=True)
    day7ex4sets = models.IntegerField(null=0)
    day7ex4reps = models.IntegerField(null=0)