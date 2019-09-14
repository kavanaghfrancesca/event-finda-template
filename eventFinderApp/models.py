from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    venue = models.CharField(max_length=200,null=True)
    location = models.CharField(max_length=200)
    start_time = models.DateTimeField('start time and date')
    end_time = models.DateTimeField('end time and date')
    categories = models.ManyToManyField('Category', related_name='events')
    def __str__(self):
        return self.title    


class Category(models.Model):
    name = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name