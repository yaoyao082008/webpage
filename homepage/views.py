from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *

# Create your views here.

def meetings(request):
        online_meets=webinar.objects.all()
        context={'meets': online_meets,}
        return render(request,'page/meetings.html',context)

def company_structure(request):
        return render(request,'education/company_structure.html')

def asset_protection(request):
        return render(request,'education/asset_protection.html')

def index(request):
        return render(request,'page/index.html')

def overview(request):
        return render(request,'education/overview.html')
def signout(request):
        logout(request)
        return redirect('/')

def join_us(request):
        return render(request,'page/join_us.html',{})

def tax(request):
        return render(request,'education/tax.html')

def savings(request):
        return render(request,'education/savings.html')

def retirement(request):
        return render(request,'education/retirement.html')

def life_insurance(request):
        return render(request,'education/insurance.html')

def investment(request):
        return render(request,'education/investment.html')

def estate_planning(request):
        return render(request,'education/estate_planning.html')

def long_term_care(request):
        return render(request,'education/long_term_care.html')

def medicare(request):
        return render(request,'education/medicare.html')



def signin(request):
        context={'login_failure':False}
        if request.method == "POST":
                username=request.POST.get('username')
                password=request.POST.get('password')

                user=authenticate(username=username,password=password)

                if user is not None:
                        login(request,user)

                        return redirect('/')
                else:
                        context['login_failure']=True
                        messages.error(request,"Invalid Credentials")

        return render(request,'signin/signin.html',context)




def signup(request):


        context={
                'email_failure':False,
                'password_failure':False,
                'username_taken':False,
                'email_taken':False,
        }

        if request.method=="POST":
                email=request.POST.get('email')
                password=request.POST.get('password')
                password_again=request.POST.get('password(again)')
                username=request.POST.get('username')

                try:
                        verifed_user.objects.get(verified_email=email)
                        if len(User.objects.filter(username=username))>=1:
                                context['username_taken']=True
                        if len(User.objects.filter(email=email))>=1:
                                context['email_taken']=True
                except:
                        context['email_failure']=True
                        messages.error(request,"your email is not verifed")

                if password==password_again and not True in context.values():

                        newuser=User.objects.create_user(username,email,password)

                        newuser.save()

                        messages.success(request,"Account Created")
                        return redirect('/signin/')
                elif password!=password_again:
                        context['password_failure']=True
                        messages.error(request,"Passwords DO not Match")



        return render(request,'signup/signup.html',context)
