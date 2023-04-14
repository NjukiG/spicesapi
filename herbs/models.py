# from django.db import models
from django.conf import settings
from django.db import models

class Herbs(models.Model):
    title = models.CharField(max_length=100)
    image = models.URLField(max_length=300)
    body = models.TextField()
    notes = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Create your models here.
