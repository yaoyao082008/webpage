from django.shortcuts import render
from django.contrib.auth.models import User
from .models import videos
from django.apps import apps
# Create your views here.


def video(request):
    
    verified = apps.get_model('homepage', 'verifed_user')
    id=request.user.id
    email=User.objects.get(id=id).email
    vid_number=verified.objects.get(verified_email=email).video_number
    vids=videos.objects.all()[:vid_number]

    context={
        'videos':vids
    }

    return render(request,'video.html',context)