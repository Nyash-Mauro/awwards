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
    profile_pic = CloudinaryField('image', default="media/", validators=[
                                  FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_name(cls, id, new_First_Name):
        cls.objects.filter(user_id=id).update(First_Name=new_First_Name)
        new_title_object = cls.objects.get(First_Name=new_First_Name)
        new_name = new_title_object.First_Name
        return new_name


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

