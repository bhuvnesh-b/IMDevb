from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from  PIL import Image
from django.dispatch import receiver
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg' , upload_to='profile_pics')
    ph_no = models.CharField(max_length=11,null=True )
    state = models.CharField(max_length=200 , null = True )
    datecreated = models.DateTimeField(auto_now_add = True , null=True)
    bio = models.TextField()
    
    def __str__(self):
        return f'{self.user.username}Profile'
    
  
            
