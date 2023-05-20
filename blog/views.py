from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import post
# Create your views here.


# def blogs(request):
#     return render(request, 'blog.html' ,{})

class blogs(ListView):
    model = post
    template_name='blog.html'

class article(DetailView):
    model=post
    template_name='article.html'