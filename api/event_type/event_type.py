from datetime import datetime

import graphene
from graphene.relay import Connection


class EventType(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    description = graphene.String()
    location = graphene.String()
    latitude = graphene.Float()
    longitude = graphene.Float()
    owner = graphene.Field("api.person_type.person_type.PersonType")
    attendees = graphene.ConnectionField(
        "api.person_type.person_type.PersonTypeConnection"
    )
    start_of_event = graphene.DateTime()
    end_of_event = graphene.DateTime()

    def __init__(
        self,
        event_id: int,
        name: str,
        description: str,
        location: str,
        latitude: float,
        longitude: float,
        owner,
        attendees,
        start_of_event: datetime,
        end_of_event: datetime,
    ):
        self.id = event_id
        self.name = name
        self.description = description
        self.location = location
        self.longitude = longitude
        self.latitude = latitude
        self.owner = owner
        self.attendees = attendees
        self.start_of_event = start_of_event
        self.end_of_event = end_of_event


class EventTypeConnection(Connection):
    class Meta:
        node = EventType
