from django.db import models

# Create your models here.

class ImagePost(models.Model):
    description = models.TextField(null=True, blank=True)
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to="static/images/")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)