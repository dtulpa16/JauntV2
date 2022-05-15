from django.urls import path, include
from client_trainers import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('', views.client_relations),
    path('new-trainer/', views.new_trainer),
    path('update-trainer/', views.update_trainer),
]