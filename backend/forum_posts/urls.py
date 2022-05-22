from django.urls import path

from forum_posts import views

urlpatterns = [
    path('get-posts/', views.get_posts),
    path('new-post/', views.new_post),
    path('update-post/<int:pk>/', views.update_post),
    path('like-post/<int:pk>/', views.like_post),
    path('get-replies/<int:post_id>/',views.get_replies),
    path('new-reply/',views.new_reply),
    path('update-reply/<int:pk>/',views.update_reply),
    path('like-reply/<int:pk>/',views.like_reply),
]
