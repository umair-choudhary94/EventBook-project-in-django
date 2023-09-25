from django.contrib import admin
from django.urls import path , include
from .views import *
urlpatterns = [
    path('', home,name='index'),
     path('book_unbook/<int:id>',bookevent,name='book_unbook'),
     path('add_event',addevent,name='add_event'),
     path('viewe_event/<int:id>',Single_event,name='viewe_event'),
     path('remove_event/<int:event_id>',delete_event,name='remove_event'),
     path('viewe_parti',view_parti,name='viewe_parti'),
     path('viewe_all_event',all_event,name='viewe_all_event'),
     path('confirm/<str:name>/<str:location>/<str:date>',confirm,name='confirm'),
     path('prompt/<int:id>',prompt,name='prompt'),
    path('event/search/', event_search, name='event_search'),



    
]
