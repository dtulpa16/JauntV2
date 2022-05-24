from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import TrainerBlog
from .serializers import TrainerBlogSerializer
from django.shortcuts import get_object_or_404
from client_trainers.models import ClientTrainer
from client_trainers.serializers import ClientTrainerSerializer
# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_posts(request):
    trainer = ClientTrainer.objects.get(client = request.user)
    relation_serializer = ClientTrainerSerializer(trainer)
    print('Trainer: ',relation_serializer.data['trainer'])
    posts = TrainerBlog.objects.filter(user = relation_serializer.data['trainer']['id'])
    serializer = TrainerBlogSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_post(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = TrainerBlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_post(request,pk):
        post = TrainerBlog.objects.get(pk=pk)
        serializer = TrainerBlogSerializer(post, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def like_post(request,pk):
        post = TrainerBlog.objects.get(pk=pk)
        post.likes = post.likes + 1
        serializer = TrainerBlogSerializer(post, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)