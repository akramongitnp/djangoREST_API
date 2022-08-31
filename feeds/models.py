from urllib import request
from django.db import models

class Data(models.Model):
    #user = request.user.first_name
    image = models.ImageField(blank=True, null=True)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_created=True)
    author = models.CharField(max_length=50, blank=True, null=True)

