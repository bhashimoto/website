from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=False)
    posted_at = models.DateTimeField(auto_now=True)