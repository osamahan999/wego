from datetime import datetime, timedelta, timezone

from chat_group.models import ChatGroup, StatusEnum
from event.models import Event, EventAttendee
from immutable_entities.immutable_event import immutable_event


class Seeder:
    @staticmethod
    def seed_events(
        immutable_events: list[immutable_event.ImmutableEvent],
    ) -> list[Event]:
        chat_groups_to_create = [
            ChatGroup(status=StatusEnum.DRAFT) for _ in immutable_events
        ]

        chat_groups = ChatGroup.objects.bulk_create(chat_groups_to_create)

        events_to_create: list[Event] = [
            Event(
                name=immutable_events[i].name,
                description=immutable_events[i].description,
                location=immutable_events[i].location,
                latitude=immutable_events[i].latitude,
                longitude=immutable_events[i].longitude,
                owner_id=immutable_events[i].owner.key,
                chat_group_id=chat_groups[i].id,
                start_of_event=datetime.now(timezone.utc) + timedelta(days=2),
            )
            for i in range(len(immutable_events))
        ]

        # preserves original order
        events = Event.objects.bulk_create(events_to_create)

        key_to_event: dict[int, list] = {
            events[i].id: [p.key for p in immutable_events[i].attendees]
            for i in range(len(events))
        }

        event_attendees = [
            EventAttendee(event_id=i, person_id=j)
            for i in key_to_event.keys()
            for j in key_to_event[i]
        ]

        EventAttendee.objects.bulk_create(event_attendees)
        return events
