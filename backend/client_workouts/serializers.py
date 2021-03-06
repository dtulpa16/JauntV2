from .models import Workout
from rest_framework import serializers


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = [
            'id',
            'user',
            'notes',
            'days_per_week',
            'day1ex1',
            'day1ex1sets',
            'day1ex1reps',
            'day1ex2',
            'day1ex2reps',
            'day1ex2sets',
            'day1ex3',
            'day1ex3sets',
            'day1ex3reps',
            'day1ex4',
            'day1ex4sets',
            'day1ex4reps',
            'day2ex1',
            'day2ex1sets',
            'day2ex1reps',
            'day2ex2',
            'day2ex2reps',
            'day2ex2sets',
            'day2ex3',
            'day2ex3sets',
            'day2ex3reps',
            'day2ex4',
            'day2ex4sets',
            'day2ex4reps',
            'day3ex1',
            'day3ex1sets',
            'day3ex1reps',
            'day3ex2',
            'day3ex2reps',
            'day3ex2sets',
            'day3ex3',
            'day3ex3sets',
            'day3ex3reps',
            'day3ex4',
            'day3ex4sets',
            'day3ex4reps',
            'day4ex1',
            'day4ex1sets',
            'day4ex1reps',
            'day4ex2',
            'day4ex2reps',
            'day4ex2sets',
            'day4ex3',
            'day4ex3sets',
            'day4ex3reps',
            'day4ex4',
            'day4ex4sets',
            'day4ex4reps',
            'day5ex1',
            'day5ex1sets',
            'day5ex1reps',
            'day5ex2',
            'day5ex2reps',
            'day5ex2sets',
            'day5ex3',
            'day5ex3sets',
            'day5ex3reps',
            'day5ex4',
            'day5ex4sets',
            'day5ex4reps',
            'day6ex1',
            'day6ex1sets',
            'day6ex1reps',
            'day6ex2',
            'day6ex2reps',
            'day6ex2sets',
            'day6ex3',
            'day6ex3sets',
            'day6ex3reps',
            'day6ex4',
            'day6ex4sets',
            'day6ex4reps',
            'day7ex1',
            'day7ex1sets',
            'day7ex1reps',
            'day7ex2',
            'day7ex2reps',
            'day7ex2sets',
            'day7ex3',
            'day7ex3sets',
            'day7ex3reps',
            'day7ex4',
            'day7ex4sets',
            'day7ex4reps',
        ]
