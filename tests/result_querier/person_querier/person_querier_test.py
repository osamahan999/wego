from unittest import TestCase
from unittest.mock import MagicMock

from immutable_entities.immutable_person import ImmutablePerson
from person.models import Person
from result_querier.person_querier.person_querier import PersonQuerier


class PersonQuerierTest(TestCase):
    def test_get_person(self):
        person_id: int = 1
        first_name: str = "first"
        last_name: str = "last"
        email: str = "email@gmail.com"
        phone_number: str = "6505555555"
        username: str = "test"

        person = Person(
            id=person_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            username=username,
        )

        expected_immutable_person = (
            ImmutablePerson.ImmutablePersonBuilder()
            .set_key(person_id)
            .set_email(email)
            .set_username(username)
            .set_first_name(first_name)
            .set_last_name(last_name)
            .set_phone_number(phone_number)
            .build()
        )

        Person.objects.get = MagicMock(return_value=person)

        self.assertEqual(PersonQuerier.get_person(person.id), expected_immutable_person)
