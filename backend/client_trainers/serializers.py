
from .models import ClientTrainer
from rest_framework import serializers

class ClientTrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientTrainer
        fields = ['id', 'client','trainer']
        depth = 1
    #client_id = serializers.IntegerField(write_only = True)