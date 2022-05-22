from django.urls import path
from trainer_blogs import views

urlpatterns = [
    path('get-reviews/', views.get_posts),
    path('new-review/', views.new_post),
]