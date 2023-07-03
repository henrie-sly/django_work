from django.db import models
from datetime import datetime
# Create your models here.

class Schedule(models.Model):
    title = models.CharField(max_length = 20)
    descript = models.CharField(max_length = 50)

class Date(models.Model):
    item = models.ForeignKey(Schedule, on_delete = models.CASCADE)
    date = models.DateField()
    on_created = models.DateTimeField(auto_now = True)