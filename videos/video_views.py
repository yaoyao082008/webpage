from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from django.apps import apps
# Create your views here.


def video(request):
    
    verified = apps.get_model('homepage', 'verifed_user')
    id=request.user.id
    email=User.objects.get(id=id).email
    person=verified.objects.get(verified_email=email)
    tax=tax_video.objects.all()[:person.tax_video_number]
    long_term_care=long_term_care_video.objects.all()[:person.long_term_care_video_number]
    retirement= retirement_video.objects.all()[:person.retirement_video_number]
    savings= savings_video.objects.all()[:person.savings_video_number]
    life_insurance= life_insurance_video.objects.all()[:person.life_insurance_video_number]
    investment=  investment_video.objects.all()[:person.investment_video_number]
    estate_planning= estate_planning_video.objects.all()[:person.estate_planning_video_number]
    medicare= medicare_video.objects.all()[:person.medicare_video_number]
    other = other_video.objects.all()[:person.other_video_number]
    exam=exam_video.objects.all()

    context={
        'tax':tax,
        'long_term_care':long_term_care,
        'retirement':retirement,
        'savings':savings,
        'life_insurance':life_insurance,
        'investment':investment,
        'estate_planning':estate_planning,
        'medicare':medicare,
        'other':other,
        'exam':exam,
    }

    return render(request,'video.html',context)