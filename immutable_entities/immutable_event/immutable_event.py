from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from api.event_type.event_type import EventType
from immutable_entities.immutable_person import immutable_person


# Immutable entity for Event
@dataclass(frozen=True)
class ImmutableEvent:
    key: Optional[int]
    name: str
    description: str
    location: str
    longitude: float
    latitude: float
    # ImmutablePerson
    owner: immutable_person.ImmutablePerson
    # ImmutablePerson
    attendees: frozenset[immutable_person.ImmutablePerson]
    start_of_event: datetime
    end_of_event: Optional[datetime]

    class ImmutableEventBuilder:
        key: Optional[int]
        name: Optional[str]
        description: Optional[str]
        location: Optional[str]
        longitude: Optional[float]
        latitude: Optional[float]
        owner: Optional[immutable_person.ImmutablePerson]
        attendees: list[immutable_person.ImmutablePerson]
        start_of_event: Optional[datetime]
        end_of_event: Optional[datetime]

        def __init__(self):
            self.key = None
            self.name = None
            self.description = None
            self.location = None
            self.latitude = None
            self.longitude = None
            self.start_of_event = None
            self.end_of_event = None
            self.owner = None
            self.attendees = []

        def set_key(self, key: int) -> "ImmutableEvent.ImmutableEventBuilder":
            self.key = key
            return self

        def set_name(self, name: str) -> "ImmutableEvent.ImmutableEventBuilder":
            self.name = name
            return self

        def set_description(
            self, description: str
        ) -> "ImmutableEvent.ImmutableEventBuilder":
            self.description = description
            return self

        def set_location(self, location: str) -> "ImmutableEvent.ImmutableEventBuilder":
            self.location = location
            return self

        def set_latitude(
            self, latitude: float
        ) -> "ImmutableEvent.ImmutableEventBuilder":
            self.latitude = latitude
            return self

        def set_longitude(
            self, longitude: float
        ) -> "ImmutableEvent.ImmutableEventBuilder":
            self.longitude = longitude
            return self

        def set_owner(
            self, owner: immutable_person.ImmutablePerson
        ) -> "ImmutableEvent.ImmutableEventBuilder":
            self.owner = owner
            return self

        def set_attendees(
            self, attendees: list[immutable_person.ImmutablePerson]
        ) -> "ImmutableEvent.ImmutableEventBuilder":
            self.attendees = attendees
            return self

        def set_start_of_event(
            self, start_of_event: datetime
        ) -> "ImmutableEvent.ImmutableEventBuilder":
            self.start_of_event = start_of_event
            return self

        def set_end_of_event(
            self, end_of_event: datetime
        ) -> "ImmutableEvent.ImmutableEventBuilder":
            self.end_of_event = end_of_event
            return self

        def build(self) -> "ImmutableEvent":
            assert self.name
            assert self.description
            assert self.location
            assert self.longitude
            assert self.latitude
            assert self.owner
            assert self.attendees
            assert self.start_of_event

            return ImmutableEvent(
                key=self.key,
                name=self.name,
                description=self.description,
                location=self.location,
                longitude=self.longitude,
                latitude=self.latitude,
                owner=self.owner,
                attendees=frozenset(self.attendees),
                start_of_event=self.start_of_event,
                end_of_event=self.end_of_event,
            )

    def to_builder(self) -> ImmutableEventBuilder:
        return (
            self.ImmutableEventBuilder()
            .set_key(self.key)
            .set_name(self.name)
            .set_description(self.description)
            .set_location(self.location)
            .set_longitude(self.longitude)
            .set_latitude(self.latitude)
            .set_owner(self.owner)
            .set_attendees(list(self.attendees))
            .set_start_of_event(self.start_of_event)
            .set_end_of_event(self.end_of_event)
        )

    def to_event_type(self) -> EventType:
        event: EventType = EventType(
            event_id=self.key,
            name=self.name,
            description=self.description,
            location=self.location,
            latitude=self.latitude,
            longitude=self.longitude,
            owner=self.owner.to_person_type(),
            attendees=[attendee.to_person_type() for attendee in self.attendees],
            start_of_event=self.start_of_event,
            end_of_event=self.end_of_event,
        )
        return event
