from datetime import datetime, timedelta, timezone

from django.db import connection
from django.test import TransactionTestCase
from django.test.utils import CaptureQueriesContext

from chat_group.models import ChatGroup, StatusEnum
from event.models import Event
from immutable_entities.immutable_event import ImmutableEvent
from person.models import Person
from result_querier.event_querier.event_querier import EventQuerier


class EventQuerierTest(TransactionTestCase):
    person: Person = None
    attendee_1: Person = None
    attendee_2: Person = None

    def setUp(self) -> None:
        self.person = Person.objects.create_user(
            username="test",
            password="test",
            first_name="test",
            last_name="test",
            email="test@gmail.com",
        )

        self.attendee_1 = Person.objects.create_user(
            username="attendee_1",
            password="attendee_1",
            first_name="attendee_1",
            last_name="attendee_1",
            email="attendee_1@gmail.com",
        )

        self.attendee_2 = Person.objects.create_user(
            username="attendee_2",
            password="attendee_2",
            first_name="attendee_2",
            last_name="attendee_2",
            email="attendee_2@gmail.com",
        )

    def test_get_owned_events(self):
        chat_group = ChatGroup.objects.create(status=StatusEnum.PUBLISHED)
        start_of_event = datetime.now(timezone.utc) + timedelta(days=2)

        event = Event.objects.create(
            name="test",
            description="description",
            chat_group_id=chat_group.id,
            owner_id=self.person.id,
            location="loc",
            latitude=3.0,
            longitude=4.0,
            start_of_event=start_of_event,
        )
        event.members.add(self.person.id)
        event.members.add(self.attendee_1)
        event.members.add(self.attendee_2)

        expected_immutable_event = (
            ImmutableEvent.ImmutableEventBuilder()
            .set_key(event.id)
            .set_name(event.name)
            .set_description(event.description)
            .set_location(event.location)
            .set_longitude(event.longitude)
            .set_latitude(event.latitude)
            .set_owner(self.person.transform_to_immutable_entity())
            .set_start_of_event(start_of_event)
            .set_attendees(
                [
                    self.attendee_1.transform_to_immutable_entity(),
                    self.attendee_2.transform_to_immutable_entity(),
                    self.person.transform_to_immutable_entity(),
                ]
            )
            .build()
        )

        with CaptureQueriesContext(connection) as context:
            self.assertEqual(
                EventQuerier.get_owned_events(self.person.id),
                frozenset([expected_immutable_event]),
            )

        self.assertEqual(len(context.captured_queries), 2)

    def test_get_attended_events(self):
        chat_group = ChatGroup.objects.create(status=StatusEnum.PUBLISHED)
        start_of_event = datetime.now(timezone.utc) + timedelta(days=2)

        event = Event.objects.create(
            name="test",
            description="description",
            chat_group_id=chat_group.id,
            owner_id=self.person.id,
            location="loc",
            latitude=3.0,
            longitude=4.0,
            start_of_event=start_of_event,
        )
        event.members.add(self.person.id)
        event.members.add(self.attendee_1)
        event.members.add(self.attendee_2)

        expected_immutable_event = (
            ImmutableEvent.ImmutableEventBuilder()
            .set_key(event.id)
            .set_name(event.name)
            .set_description(event.description)
            .set_location(event.location)
            .set_longitude(event.longitude)
            .set_latitude(event.latitude)
            .set_owner(self.person.transform_to_immutable_entity())
            .set_attendees(
                [
                    self.attendee_1.transform_to_immutable_entity(),
                    self.attendee_2.transform_to_immutable_entity(),
                    self.person.transform_to_immutable_entity(),
                ]
            )
            .set_start_of_event(start_of_event)
            .build()
        )

        with CaptureQueriesContext(connection) as context:
            self.assertEqual(
                EventQuerier.get_attended_events(
                    self.person.id, only_future_events=False
                ),
                frozenset([expected_immutable_event]),
            )

        self.assertEqual(len(context.captured_queries), 2)
