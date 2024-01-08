from django.urls import path
from . import views
urlpatterns = [
    path('english-videos/', views.video, name='english_video'),
]