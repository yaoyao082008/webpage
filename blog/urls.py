

from django.urls import path

#from . import views

from .views import blogs,article


urlpatterns=[
    #path('blogs/',views.blogs,name="blogs")
    path('blogs/', blogs.as_view(),name='blogs'),
    path('article/<int:pk>',article.as_view(),name='article')
]