from django.urls import path,include
from . import views


urlpatterns=[
    path("",views.index),
    path("webpage/",include("webpage.urls"))
    ]