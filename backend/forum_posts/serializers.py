from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import ForumPost
from .models import ForumReply

class ForumPostSerializer(serializers.ModelSerializers):
    class Meta:
        model = ForumPost
        fields = ['id','user','body','likes']

class ForumReplySerializer(serializers.ModelSerializers):
    class Meta:
        model = ForumReply
        fields = ['id','post','user','likes']
        depth = 2