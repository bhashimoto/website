from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Habit(models.Model):
  
    name = models.CharField(max_length=100, blank=False)

    sunday = models.BooleanField(default=False)
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    
    start_at = models.DateField(default=datetime.now)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class Record(models.Model):
    date = models.DateField(default=datetime.now)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)