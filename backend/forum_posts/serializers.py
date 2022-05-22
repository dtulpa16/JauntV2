
from rest_framework import serializers
from .models import ForumPost
from .models import ForumReply

class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = ['id','user','body','likes']

class ForumReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumReply
        fields = ['id','post','user','likes']
        depth = 2
    post_id = serializers.IntegerField(write_only = True)