from .models import TrainerBlog
from rest_framework import serializers

class TrainerBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerBlog
        fields = ['id','user','body','likes']
        depth = 1