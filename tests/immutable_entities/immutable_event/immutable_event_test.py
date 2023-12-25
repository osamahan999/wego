from unittest import TestCase

from immutable_entities.immutable_event import ImmutableEvent


class ImmutableEventTest(TestCase):
    def test_immutable_event_builder(self):
        key: int = 1
        name: str = "name"
        description: str = "description"
        location: str = "location"
        latitude: float = 3.0
        longitude: float = 3.0
        owner_id: int = 2
        attendee_ids: list[int] = [3, 4]

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
            .set_owner_id(owner_id)
            .set_attendee_ids(attendee_ids)
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
        self.assertEqual(event.owner_id, owner_id)
        self.assertEqual(event.attendee_ids, frozenset(attendee_ids))

        # to_builder
        self.assertIsInstance(event.to_builder(), ImmutableEvent.ImmutableEventBuilder)

        # Assert data integrity from class to builder
        self.assertEqual(event.to_builder().key, key)
        self.assertEqual(event.to_builder().name, name)
        self.assertEqual(event.to_builder().description, description)
        self.assertEqual(event.to_builder().location, location)
        self.assertEqual(event.to_builder().latitude, latitude)
        self.assertEqual(event.to_builder().longitude, longitude)
        self.assertEqual(event.to_builder().owner_id, owner_id)
        self.assertEqual(set(event.to_builder().attendee_ids), set(attendee_ids))
