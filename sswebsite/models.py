from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    certiTitle = models.CharField(max_length=255)
    file = models.FileField(upload_to='user_uploads')
    certDescription = models.TextField
    skills = models.CharField(max_length=255)
    is_visible = models.BooleanField(default=True)
    