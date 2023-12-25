from dataclasses import dataclass
from typing import Optional


# Immutable entity for Event
@dataclass(frozen=True)
class Event:
    key: str
    name: str
    description: str
    location: str
    longitude: float
    latitude: float
    owner_id: str
    attendee_ids: frozenset[str]

    class EventBuilder:
        key: Optional[str]
        name: Optional[str]
        description: Optional[str]
        location: Optional[str]
        longitude: Optional[float]
        latitude: Optional[float]
        owner_id: Optional[str]
        attendee_ids: list[str]

        def __init__(self):
            self.key = None
            self.name = None
            self.description = None
            self.location = None
            self.latitude = None
            self.longitude = None
            self.owner_id = None
            self.attendee_ids = []

        def set_key(self, key: str) -> "Event.EventBuilder":
            self.key = key
            return self

        def set_name(self, name: str) -> "Event.EventBuilder":
            self.name = name
            return self

        def set_description(self, description: str) -> "Event.EventBuilder":
            self.description = description
            return self

        def set_location(self, location: str) -> "Event.EventBuilder":
            self.location = location
            return self

        def set_latitude(self, latitude: float) -> "Event.EventBuilder":
            self.latitude = latitude
            return self

        def set_longitude(self, longitude: float) -> "Event.EventBuilder":
            self.longitude = longitude
            return self

        def set_owner_id(self, owner_id: str) -> "Event.EventBuilder":
            self.owner_id = owner_id
            return self

        def set_attendee_ids(self, attendee_ids: list[str]) -> "Event.EventBuilder":
            self.attendee_ids = attendee_ids
            return self

        def build(self) -> "Event":
            assert self.key
            assert self.name
            assert self.description
            assert self.location
            assert self.longitude
            assert self.latitude
            assert self.owner_id
            assert self.attendee_ids

            return Event(
                key=self.key,
                name=self.name,
                description=self.description,
                location=self.location,
                longitude=self.longitude,
                latitude=self.latitude,
                owner_id=self.owner_id,
                attendee_ids=frozenset(self.attendee_ids),
            )

    def to_builder(self) -> EventBuilder:
        return (
            self.EventBuilder()
            .set_key(self.key)
            .set_name(self.name)
            .set_description(self.description)
            .set_location(self.location)
            .set_longitude(self.longitude)
            .set_latitude(self.latitude)
            .set_owner_id(self.owner_id)
            .set_attendee_ids(list(self.attendee_ids))
        )
