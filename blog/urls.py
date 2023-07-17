

from django.urls import path

#from . import views

from .views import blogs,article
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    #path('blogs/',views.blogs,name="blogs")
    path('blogs/', blogs.as_view(),name='blogs'),
    path('article/<int:pk>',article.as_view(),name='article')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
