from django.urls import path, include
from client_workouts import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('get-workout/', views.get_workout),
    path('new-workout/', views.new_workout),
    path('update-workout/<int:id>/', views.update_workout),
]