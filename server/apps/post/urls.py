from django.urls import path
from apps.post import views as post_views

urlpatterns = [
    path('posts/<int:pk>/', post_views.posts_view),
    path('likes/<int:pk>/', post_views.likes_view)
]