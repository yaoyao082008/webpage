from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from django.apps import apps
# Create your views here.

@login_required
def video(request):
    
    verified = apps.get_model('homepage', 'everyone_video_number')
    num=verified.objects.first()
    tax=tax_video.objects.all()[:num.Tax_Video_Number]
    long_term_care=long_term_care_video.objects.all()[:num.Long_Term_Care_Video_number]
    retirement= retirement_video.objects.all()[:num.Retirement_Video_Number]
    savings= college_university_savings_video.objects.all()[:num.Savings_Video_Number]
    life_insurance= life_insurance_video.objects.all()[:num.Life_Insurance_Video_Number]
    asset_protection=  asset_protection_video.objects.all()[:num.Asset_Protection_Video_Number]
    estate_planning= estate_planning_video.objects.all()[:num.Estate_Planning_Video_Number]
    medicare= medicare_video.objects.all()[:num.Medicare_Video_Number]
    RealEstate= Real_Estate_Investment_Video.objects.all()[:num.Real_Estate_Investment_Video_Number]
    General= General_Financial_Planning_Video.objects.all()[:num.General_Financial_Planning_Video_Number]
    CompanyStructure= Company_Structure_Video.objects.all()[:num.Company_Structure_Video_Number]
    other = other_video.objects.all()[:num.Other_Video_Number]
    exam=exam_video.objects.all()

    context={
        'tax':tax,
        'long_term_care':long_term_care,
        'retirement':retirement,
        'savings':savings,
        'life_insurance':life_insurance,
        'asset_protection':asset_protection,
        'estate_planning':estate_planning,
        'medicare':medicare,
        'other':other,
        'real_estate':RealEstate,
        'General':General,
        'company_structure':CompanyStructure,
        'exam':exam,
    }

    return render(request,'video.html',context)