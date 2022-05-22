from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Workout
from .serializers import WorkoutSerializer
from django.shortcuts import get_object_or_404
# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_workout(request):
    trainer = get_object_or_404(Workout, user = request.user)
    serializer = WorkoutSerializer(trainer)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_workout(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = WorkoutSerializer(data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_workout(request,id):
        workout = Workout.objects.filter(user = id)
        serializer = WorkoutSerializer(workout, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.update(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)