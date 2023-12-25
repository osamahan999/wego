from unittest import TestCase

from immutable_entities.event import Event


class EventTest(TestCase):
    def test_event_builder(self):
        key: str = "key"
        name: str = "name"
        description: str = "description"
        location: str = "location"
        latitude: float = 3.0
        longitude: float = 3.0
        owner_id: str = "mediakey"
        attendee_ids: list[str] = ["string1", "string2"]

        # Assert that EventBuilder constructor works
        self.assertIsNotNone(Event.EventBuilder())
        self.assertIsInstance(Event.EventBuilder(), Event.EventBuilder)

        # Assert that EventBuilder.build
        event: Event = (
            Event.EventBuilder()
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
        self.assertIsInstance(event.to_builder(), Event.EventBuilder)

        # Assert data integrity from class to builder
        self.assertEqual(event.to_builder().key, key)
        self.assertEqual(event.to_builder().name, name)
        self.assertEqual(event.to_builder().description, description)
        self.assertEqual(event.to_builder().location, location)
        self.assertEqual(event.to_builder().latitude, latitude)
        self.assertEqual(event.to_builder().longitude, longitude)
        self.assertEqual(event.to_builder().owner_id, owner_id)
        self.assertEqual(set(event.to_builder().attendee_ids), set(attendee_ids))
