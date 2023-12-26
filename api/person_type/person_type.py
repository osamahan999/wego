import graphene

from immutable_entities.immutable_person import ImmutablePerson


class PersonType(graphene.ObjectType):
    id = graphene.Int()
    username = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()
    phone_number = graphene.String()

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

    @staticmethod
    def get_person_type(immutable_person: ImmutablePerson) -> "PersonType":
        person: PersonType = PersonType(
            person_id=immutable_person.key,
            username=immutable_person.username,
            first_name=immutable_person.first_name,
            last_name=immutable_person.last_name,
            email=immutable_person.email,
            phone_number=immutable_person.phone_number,
        )
        return person
