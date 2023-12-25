from django.db import models

from person.models import Person


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=350)
    owner = models.ForeignKey(Person, on_delete=models.PROTECT)
    members = models.ManyToManyField(
        Person, related_name="events", through="EventAttendee"
    )
    location = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()
    # TODO add a photos ManyToMany field.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class EventAttendee(models.Model):
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
