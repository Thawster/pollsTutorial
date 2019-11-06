# myclub_project\events\models.py

from django.db import models
class ClubUser(models.Model):
     first_name = models.CharField(max_length=30)
     last_name = models.CharField(max_length=30)
 
     def __str__(self):
         return self.first_name + " " + self.last_name
        
class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.CharField(max_length=120)
    manager = models.CharField(max_length = 60)
    attendees = models.ManyToManyField(ClubUser)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


