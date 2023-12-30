from datetime import datetime, timedelta, timezone
from unittest import TestCase

from immutable_entities.immutable_event import ImmutableEvent
from immutable_entities.immutable_person import ImmutablePerson


class ImmutableEventTest(TestCase):
    def test_immutable_event_builder(self):
        key: int = 1
        name: str = "name"
        description: str = "description"
        location: str = "location"
        latitude: float = 3.0
        longitude: float = 3.0
        owner: ImmutablePerson = (
            ImmutablePerson.ImmutablePersonBuilder()
            .set_username("test")
            .set_key(1)
            .set_email("x@gmail.com")
            .build()
        )
        attendees: list[ImmutablePerson] = [
            (
                ImmutablePerson.ImmutablePersonBuilder()
                .set_username("test2")
                .set_key(2)
                .set_email("x2@gmail.com")
                .build()
            ),
            (
                ImmutablePerson.ImmutablePersonBuilder()
                .set_username("test3")
                .set_key(3)
                .set_email("x3@gmail.com")
                .build()
            ),
        ]
        start_of_event = datetime.now(timezone.utc) + timedelta(days=2)

        # Assert that EventBuilder constructor works
        self.assertIsNotNone(ImmutableEvent.ImmutableEventBuilder())
        self.assertIsInstance(
            ImmutableEvent.ImmutableEventBuilder(), ImmutableEvent.ImmutableEventBuilder
        )

        # Assert that EventBuilder.build
        event: ImmutableEvent = (
            ImmutableEvent.ImmutableEventBuilder()
            .set_key(key)
            .set_name(name)
            .set_description(description)
            .set_location(location)
            .set_longitude(longitude)
            .set_latitude(latitude)
            .set_owner(owner)
            .set_attendees(attendees)
            .set_start_of_event(start_of_event)
            .build()
        )

        # assert data integrity from builder to class
        self.assertIsNotNone(event)
        self.assertEqual(event.key, key)
        self.assertEqual(event.name, name)
        self.assertEqual(event.description, description)
        self.assertEqual(event.location, location)
        self.assertEqual(event.latitude, latitude)
        self.assertEqual(event.longitude, longitude)
        self.assertEqual(event.owner, owner)
        self.assertEqual(event.attendees, frozenset(attendees))
        self.assertEqual(event.start_of_event, start_of_event)

        # to_builder
        self.assertIsInstance(event.to_builder(), ImmutableEvent.ImmutableEventBuilder)

        # Assert data integrity from class to builder
        self.assertEqual(event.to_builder().key, key)
        self.assertEqual(event.to_builder().name, name)
        self.assertEqual(event.to_builder().description, description)
        self.assertEqual(event.to_builder().location, location)
        self.assertEqual(event.to_builder().latitude, latitude)
        self.assertEqual(event.to_builder().longitude, longitude)
        self.assertEqual(event.to_builder().owner, owner)
        self.assertEqual(set(event.to_builder().attendees), set(attendees))
        self.assertEqual(event.to_builder().start_of_event, start_of_event)
