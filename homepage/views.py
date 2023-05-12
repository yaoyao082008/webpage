from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *

# Create your views here.
"""
        how to implement video system:

        first check if the user is authenticated 
        if they are get their email
        filter their email in their verifed user 
        verified user will have an video number on them
        then call video.objects.all[:verified_user.objects.filter(email=email).video_number]
"""


"""
        get current user email:

        if request.user.is_authenticated:
                identification=request.user.id
                user=User.objects.get(id=identification)
                email=user.email
        else:
                email='not logged in'
"""
def index(request):
        context={'meeting': meetings.objects.all()}
        return render(request,'page/index.html',context)

def contact(request):
        return render(request,'page/contact.html')

def videos(request):
        identification=request.user.id
        user=User.objects.get(id=identification)
        email=user.email
        vid_number=verifed_user.objects.get(verified_email=email).video_number
        videos=video.objects.all()[:vid_number]
        return render(request,'page/videos.html',{'videos':videos})
        
def signout(request):
        logout(request)
        return redirect('/')


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
