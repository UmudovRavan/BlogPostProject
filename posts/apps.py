from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'


from django.urls import path
from . import views

urlpatterns = [
    # Digər URL-lər
    path('tags/', views.tags_list, name='tags_list'),
]

     