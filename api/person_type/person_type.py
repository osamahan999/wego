import graphene

from result_querier.event_querier.event_querier import EventQuerier


class PersonType(graphene.ObjectType):
    id = graphene.Int()
    username = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()
    phone_number = graphene.String()
    owned_events = graphene.ConnectionField(
        "api.event_type.event_type.EventTypeConnection"
    )

    def __init__(
        self,
        person_id: int,
        username: str,
        first_name: str,
        last_name: str,
        email: str,
        phone_number: str,
    ) -> None:
        self.id = person_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def resolve_owned_events(self):
        return [
            immutable_event.to_event_type()
            for immutable_event in EventQuerier.get_owned_events(self.id)
        ]
