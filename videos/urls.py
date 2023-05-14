from django.urls import path
from . import video_views

urlpatterns = [
    path('videos/', video_views.video, name='video'),
    
]
