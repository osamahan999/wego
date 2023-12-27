import graphene
from graphene.relay import Connection

from api.person_type.person_type import PersonType


class EventType(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    description = graphene.String()
    location = graphene.String()
    latitude = graphene.Float()
    longitude = graphene.Float()
    owner = graphene.Field(PersonType)

    def __init__(
        self,
        event_id: int,
        name: str,
        description: str,
        location: str,
        latitude: float,
        longitude: float,
        owner: PersonType,
        attendees: list[PersonType],
    ):
        self.id = event_id
        self.name = name
        self.description = description
        self.location = location
        self.longitude = longitude
        self.latitude = latitude
        self.owner = owner
        self.attendees = attendees


class EventTypeConnection(Connection):
    class Meta:
        node = EventType
