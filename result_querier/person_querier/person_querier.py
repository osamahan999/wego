from immutable_entities.immutable_person import ImmutablePerson
from person.models import Person


class PersonQuerier:
    @staticmethod
    def get_person(key: id) -> ImmutablePerson:
        # Throws django.ObjectDoesNotExist
        person: Person = Person.objects.get(id=key)
        return PersonQuerier.transform_to_immutable_entity(person)

    @staticmethod
    def transform_to_immutable_entity(person: Person) -> ImmutablePerson:
        person_builder: ImmutablePerson.ImmutablePersonBuilder = (
            ImmutablePerson.ImmutablePersonBuilder()
        )
        return (
            person_builder.set_key(person.id)
            .set_email(person.email)
            .set_username(person.username)
            .set_phone_number(person.phone_number)
            .set_first_name(person.first_name)
            .set_last_name(person.last_name)
            .build()
        )
