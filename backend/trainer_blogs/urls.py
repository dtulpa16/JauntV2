from django.urls import path

from trainer_blogs import views

urlpatterns = [
    path('get-posts/', views.get_posts),
    path('new-post/', views.new_post),
    path('update-post/<int:pk>/', views.update_post),
    path('like-post/<int:pk>/', views.like_post),
]