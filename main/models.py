from django.db import models
from django.contrib.auth.models import User
import math
import datetime
class event_catagorey(models.Model):
    name = models.TextField(max_length=100) 
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)
class event(models.Model):
    EVENT_TYPES = (
        ('in_person', 'In-Person'),
        ('online', 'Online'),
    )
    name = models.TextField(max_length=100) 
    description=models.TextField()
    orginzer=models.ForeignKey(User,models.CASCADE,related_name='orgnizer')
    participants=models.ManyToManyField(User,default=None,blank=True)
    city = models.TextField(max_length=200,default='')
    state = models.TextField(max_length=200,default='')
    date = models.DateField()
    educational_leave = models.BooleanField(default=False)
    max_participants = models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES, default='in_person')
    tags = models.ManyToManyField(Tag)  


    def __str__(self):
        return str(self.name)
    @property
    def num_likes(self):
        return self.participants.all().count()
    @property
    def remain(self):
        book=self.participants.all().count()
        total=self.max_participants-book
        return total
    @property
    def location(self):
       
        return str(self.city)+', '+str(self.state)
    @property
    def ago(self):
        now = datetime.datetime.now(datetime.timezone.utc)
        
        diff= now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

            

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"

            
