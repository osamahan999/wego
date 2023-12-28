from __future__ import annotations

from immutable_entities.immutable_person import immutable_person
from person.models import Person


class PersonQuerier:
    @staticmethod
    def get_immutable_person(key: int) -> immutable_person.ImmutablePerson:
        person: Person = Person.objects.get(id=key)
        return person.transform_to_immutable_entity()
