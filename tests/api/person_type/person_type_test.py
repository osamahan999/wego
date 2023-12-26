from unittest import TestCase

from api.person_type.person_type import PersonType
from immutable_entities.immutable_person import ImmutablePerson


class PersonTypeTest(TestCase):
    def test_get_person_type(self):
        key: int = 1
        username = "username"
        first_name = "first"
        last_name = "last"
        email = "email"
        phone_number = "6"

        person: ImmutablePerson = (
            ImmutablePerson.ImmutablePersonBuilder()
            .set_key(key)
            .set_username(username)
            .set_first_name(first_name)
            .set_last_name(last_name)
            .set_phone_number(phone_number)
            .set_email(email)
            .build()
        )

        expected_person_type = PersonType(
            person_id=key,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
        )

        self.assertEqual(PersonType.get_person_type(person), expected_person_type)
