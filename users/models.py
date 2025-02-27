
from django.db import models 
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profile_picture',default='')
    location=models.CharField(max_length=100)


# class Tweet(models.Model):
#     photo = models.ImageField(upload_to='tweets/')



    def __str__(self):
        return self.user.username