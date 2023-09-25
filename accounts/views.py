from typing import Generic
from django.core import signing
from django.http import response
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import SignUpForm
from verify_email.email_handler import send_verification_email
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import profile
from main.models import event
from django.contrib.auth.models import Group

import os
# Create your views here.
def login_request(request):
    form = AuthenticationForm()
    return render(request = request,template_name = "registration/login.html",context={"form":form})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email=request.POST.get('email')
            if User.objects.filter(email=email).exists():
                msg='Email Alredy Exist Please Try Another'
                return render(request, 'registration/emailExist.html', {'msg': msg})
            else:
                inactive_user = send_verification_email(request, form)
                role=request.POST.get('role')
                group = Group.objects.get(name=role)
                inactive_user.groups.add(group)
                email=request.POST.get('email')
                
                msg='please check your mail to acctivate accout'
                return render(request, 'registration/success.html', {'msg': msg,'mail':email})

    else:
        form =SignUpForm()
    return render(request, 'registration/register.html', {'form': form})


    
def viewProfile(request):
    events=event.objects.filter(orginzer=request.user)
    print(events)
    return render(request,'profile/profile.html',context={'events':events})

def view_user_profile(request,user_id):
    userobj=User.objects.get(id=user_id)
    events=event.objects.filter(orginzer=userobj)
    context={'userInfo':userobj,'events':events}
    return render(request,'profile/viewe_profile.html',context)
@csrf_exempt
def updateinfo(request):
    data=dict()
    if request.method=='POST':
        fn=request.POST.get('fn')
        ln=request.POST.get('ln')
        em=request.POST.get('em')
        un=request.POST.get('un')
        obj=User.objects.get(pk=request.user.id)
        obj.first_name=fn
        obj.last_name=ln
        obj.email=em
        obj.username=un
        obj.save()
        data={'firstName':obj.first_name,'lastName':obj.last_name,'email':obj.email,'uname':obj.username}
        return JsonResponse({'status':1,'msg':'User Updated Successfully!','obj':data})

@csrf_exempt
def updatePic(request):
    data=dict()
    if request.method=='POST':
         
         obj=profile.objects.get(user=request.user)
         image=request.FILES.get('profilePic')
         obj.profilePic=image
         obj.save()
         image_url=obj.profilePic.url
         return JsonResponse({'status':1,'img':image_url})

@csrf_exempt
def follow(request):
    if request.method=='POST':
        follower=request.user
        userID=request.POST.get('userID')
        status=""
        followed=profile.objects.get(user=userID)

        if follower not in followed.followers.all():
            followed.followers.add(follower)
            status=1 #return 1 if follow
        else:
            followed.followers.remove(follower)
            status=0 #retur 0 if unfollow
        return JsonResponse({'status':status})


@csrf_exempt
def updateProfile(request):
    data=dict()
    if request.method=='POST':
        bio=request.POST.get('bio')
        mb=request.POST.get('mb')
        pf=profile.objects.get(user_id=request.user.id)
        pf.bio=bio
        pf.phone=mb
        pf.save()
        data={'bio':bio,'mobile':mb}
        return JsonResponse({'status':1,'msg':'User Updated Successfully!','obj':data})


@csrf_exempt
def updateCompany(request):
    data=dict()
    if request.method=='POST':
        name=request.POST.get('company_name')
        description=request.POST.get('profile_description')
        pf=profile.objects.get(user_id=request.user.id)
        pf.company_name=name
        pf.description=description
        pf.save()
        data={'name':name,'description':description}
        return JsonResponse({'status':1,'msg':'Company Updated Successfully!','obj':data})