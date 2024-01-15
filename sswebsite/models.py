from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    certificate_name = models.CharField(max_length=255)
    file = models.FileField(upload_to='user_uploads/')
    is_visible = models.BooleanField(default=True)
    certificate_desc = models.TextField(default='')  
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    current_position = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length = 15, blank = True, null = True)