from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import OneToOneField
from django.db.models.signals import post_save
# Create your models here.
from django.contrib.auth.models import AbstractUser


class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(null=True)
    description=models.TextField(max_length=500,default='',null=True,blank=True)
    phone=models.CharField(max_length=20,null=True)
    profilePic=models.ImageField(upload_to='media/profile', default='def.jpg')
    company_name=models.CharField(max_length=100,default='',null=True,blank=True)
    
    def __str__(self):
        return str(self.user)


def create_profile(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(user=instance)
        print('created profile Done')

post_save.connect(create_profile,sender=User)


