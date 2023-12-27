from django.db.models import QuerySet

from event.models import Event, EventAttendee
from immutable_entities.immutable_event import ImmutableEvent


class EventQuerier:
    @staticmethod
    def get_owned_events(person_id: int) -> frozenset[ImmutableEvent]:
        owned_events: QuerySet[Event] = (
            Event.objects.filter(owner_id=person_id)
            .select_related("owner")
            .prefetch_related("members")
        )

        return frozenset(
            [event.transform_to_immutable_entity() for event in owned_events]
        )

    @staticmethod
    def get_attended_events(person_id: int):
        # Two queries currently :( not sure how to write the django to just inner join & filter
        events_attended = EventAttendee.objects.select_related(
            "event", "event__owner"
        ).filter(person_id=person_id)
        events = [attended.event for attended in events_attended]
        return frozenset([event.transform_to_immutable_entity() for event in events])

    @staticmethod
    def transform_to_immutable_entity(event: Event) -> ImmutableEvent:
        event_builder: ImmutableEvent.ImmutableEventBuilder = (
            ImmutableEvent.ImmutableEventBuilder()
        )

        return (
            event_builder.set_key(event.id)
            .set_name(event.name)
            .set_description(event.description)
            .set_location(event.location)
            .set_longitude(event.longitude)
            .set_latitude(event.latitude)
            .set_owner(event.owner.transform_to_immutable_entity())
            .set_attendees(
                [
                    member.transform_to_immutable_entity()
                    for member in event.members.all()
                ]
            )
            .build()
        )
