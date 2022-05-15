from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import ClientTrainer
from .serializers import ClientTrainerSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def client_relations(request):
    trainer = ClientTrainer.objects.filter(client = request.user.id)
    serializer = ClientTrainerSerializer(trainer)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_trainer(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = ClientTrainerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_trainer(request):
        client = ClientTrainer.objects.filter(client = request.user.id)
        serializer = ClientTrainerSerializer(client, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.update(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)