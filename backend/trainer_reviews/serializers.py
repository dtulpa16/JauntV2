from .models import TrainerReview
from rest_framework import serializers

class TrainerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerReview
        fields = ['id','user', 'trainer','body','rating']
        depth = 1
    trainer_id = serializers.IntegerField(write_only = True)