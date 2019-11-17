from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    start_date = models.DateField('start date')
    end_date = models.DateField('end date')
    start_time = models.TimeField('start time')
    end_time = models.TimeField('end time')
    categories = models.ManyToManyField('Category', related_name='events')
    host = models.ForeignKey(User, related_name='hosting_events', on_delete = models.CASCADE)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    