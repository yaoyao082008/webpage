"""
URL configuration for webpage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('signout/',views.signout,name='signout'),
    path('joinus/',views.join_us,name='join_us'),
    path('tax/',views.tax,name='tax'),
    path('savings/',views.savings,name='savings'),
    path('retirement/',views.retirement,name='retirement'),
    path('lifeinsurance/',views.life_insurance,name='life_insurance'),
    path('investment/',views.investment,name='investment'),
    path('estateplanning/',views.estate_planning,name='estate_planning'),
    path('longtermcare/',views.long_term_care,name='long_term_care'),
    path('medicare/',views.medicare,name='medicare'),
    path('overview/',views.overview,name='overview'),
    path('asset-protection/',views.asset_protection,name='asset_protection'),
    path('company-structure/',views.company_structure,name='company_structure'),
    path('inner-meetings/',views.inner_meetings,name='inner-meetings'),
    path('eng-meetings/',views.eng_meetings,name='eng-meetings'),
    path('ch-meetings/',views.ch_meetings,name='ch-meetings'),
    path('contacts/',views.contact,name='contacts'),
    # path('licensed-page/',views.licensed_page,name='licensed-page')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
