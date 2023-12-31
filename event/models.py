from __future__ import annotations

from django.db import models

from chat_group.models import ChatGroup
from immutable_entities.immutable_event import immutable_event


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=350)
    chat_group = models.ForeignKey(ChatGroup, on_delete=models.PROTECT)
    owner = models.ForeignKey("person.Person", on_delete=models.PROTECT)
    # Members contains the owner as well.
    members = models.ManyToManyField(
        "person.Person", related_name="events", through="EventAttendee"
    )
    location = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()
    start_of_event = models.DateTimeField(null=False)
    end_of_event = models.DateTimeField(null=True)
    # TODO add a photos ManyToMany field.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def transform_to_immutable_entity(self) -> immutable_event.ImmutableEvent:
        event_builder: immutable_event.ImmutableEvent.ImmutableEventBuilder = (
            immutable_event.ImmutableEvent.ImmutableEventBuilder()
        )

        return (
            event_builder.set_key(self.id)
            .set_name(self.name)
            .set_description(self.description)
            .set_location(self.location)
            .set_longitude(self.longitude)
            .set_latitude(self.latitude)
            .set_owner(self.owner.transform_to_immutable_entity())
            .set_attendees(
                [
                    member.transform_to_immutable_entity()
                    for member in self.members.all()
                ]
            )
            .set_start_of_event(self.start_of_event)
            .set_end_of_event(self.end_of_event)
            .build()
        )


class EventAttendee(models.Model):
    person = models.ForeignKey("person.Person", on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
