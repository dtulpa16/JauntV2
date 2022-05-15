from django.contrib import admin
from .models import ForumPost
from .models import ForumReply
# Register your models here.
admin.site.register(ForumPost)
admin.site.register(ForumReply)
