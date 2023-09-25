from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.contrib.auth.decorators import login_required
from . models import *
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.utils import timezone
from datetime import datetime
from django.contrib import messages
from django.db.models import Q

from django.http import JsonResponse
from django.urls import reverse
def home(request):
    
    events=event.objects.all().order_by('-created_at')[:10]
    print(events)
    
    return render(request,'index.html',context={'events':events})

def confirm(request, name,location,date):
    detail={'name':name,'location':location,'date':date}
    return render(request,'index.html',context={'detail':detail})
def prompt(request,id):
    event_id=id
    even=event.objects.get(pk=event_id)
    detail={'pk':even.pk,'name':even.name,'location':even.location,'date':even.date}
    temp='prompt.html'
    
    return render(request,temp,context={'detail':detail})


def bookevent(request,id):
    event_id=id
    even=event.objects.get(pk=event_id)
    temp=''
    detail=None
    if request.user not in even.participants.all():
        even.participants.add(request.user)
        detail={'pk':even.pk,'name':even.name,'location':even.location,'date':even.date}
        temp='confirm.html'
    else:
        even.participants.remove(request.user)
        temp='unbooked.html'
    return render(request,temp,context={'detail':detail})
    
def Single_event(request,id):
    event_id=id
    even=event.objects.get(pk=event_id) 
    return render(request,'singal.html',context={'detail':even})
def addevent(request):
    if request.method == 'POST':
        orgnizer = request.user
        name = request.POST.get('name')
        description = request.POST.get('description')
        city = request.POST.get('city')
        state = request.POST.get('state')
        date = request.POST.get('date')
        leave = request.POST.get('is_leave')
        max_p = request.POST.get('max_p')
        event_type = request.POST.get('event_type')
        tags = request.POST.getlist('tags[]')

        if leave == 'on':
            leave = True
        else:
            leave = False

        datetime_obj = datetime.strptime(date, '%Y-%m-%d')
        timezone_obj = timezone.make_aware(datetime_obj, timezone.get_current_timezone())

        new_event = event.objects.create(
            name=name,
            description=description,
            orginzer=orgnizer,
            city=city,
            state=state,
            date=timezone_obj,
            educational_leave=leave,
            max_participants=max_p,
            event_type=event_type
        )
        new_event.tags.set(tags)  # Associate the selected tags with the new event

        messages.success(request, "Event created successfully!")
        return redirect('/viewe_all_event')

    
      
def delete_event(request,event_id):
     event.objects.get(pk=event_id).delete()
     messages.success(request, "Event deleted successfully!")
     return HttpResponseRedirect('/accounts/profile')


@csrf_exempt
def view_parti(request):
    event_id=request.POST.get('event_id')
    even=event.objects.get(pk=event_id)
    full_response='No Participants'

    if even.num_likes>0:
         full_response = ''
    for p in even.participants.all():
         view_profile = reverse('view_user_profile', args=[p.pk])
         strres=f'<li class="list-group-item"><a href="{view_profile}" style="text-decoration: none;"><img src="{ p.profile.profilePic.url }" style="width: 30px; height: 30px; border-radius:50%;"><span class="mx-2 text-muted" style="font-size:9pt;">{p.first_name} {p.last_name}</span></a></li>'
         full_response = full_response+strres
    return JsonResponse({'status':full_response})

def all_event(request):
    events = event.objects.all().order_by('-id')
    tags = Tag.objects.all()
    return render(request, 'events.html', context={'events': events, 'tags': tags})



def event_search(request):
    if request.method == 'POST':
        city = request.POST.get('city', '')
        distance = request.POST.get('distance', '')
        tags = request.POST.getlist('tags[]')  # Get a list of selected tags

        events = event.objects.all()

        # Apply filters based on city and distance
        if city and distance:
            events = events.filter(Q(city__icontains=city))

        # Apply filters based on tags
        if tags:
            events = events.filter(tags__name__in=tags)

        # Prepare the search results
        search_results = {
            'events': events
        }

        # Render the events.html template with the search results
        return render(request, 'events.html', search_results)
    tags = Tag.objects.all()
    events = event.objects.all().order_by('-id')
    return render(request, 'events.html', context={'events': events,"tags":tags})