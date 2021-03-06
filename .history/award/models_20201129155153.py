from django.db import models
import datetime as dt 
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    bio = HTMLField()
    profile_pic = CloudinaryField('image', default="media/", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    