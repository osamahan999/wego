from unittest import TestCase

from immutable_entities.immutable_person import ImmutablePerson


class PersonTest(TestCase):
    def test_person_builder(self):
        key: str = "key"
        username: str = "username"
        first_name: str = "name"
        last_name: str = "last"
        email: str = "email"
        phone_number: str = "6505155555"

        # Assert that PersonBuilder constructor works
        self.assertIsNotNone(ImmutablePerson.ImmutablePersonBuilder())
        self.assertIsInstance(
            ImmutablePerson.ImmutablePersonBuilder(),
            ImmutablePerson.ImmutablePersonBuilder,
        )

        # Assert that PersonBuilder.build
        person: ImmutablePerson = (
            ImmutablePerson.ImmutablePersonBuilder()
            .set_key(key)
            .set_username(username)
            .set_first_name(first_name)
            .set_last_name(last_name)
            .set_email(email)
            .set_phone_number(phone_number)
            .build()
        )

        # assert data integrity from builder to class
        self.assertIsNotNone(person)
        self.assertEqual(person.key, key)
        self.assertEqual(person.first_name, first_name)
        self.assertEqual(person.last_name, last_name)
        self.assertEqual(person.username, username)
        self.assertEqual(person.phone_number, phone_number)
        self.assertEqual(person.email, email)

        # to_builder
        self.assertIsInstance(
            person.to_builder(), ImmutablePerson.ImmutablePersonBuilder
        )

        # Assert data integrity from class to builder
        self.assertEqual(person.to_builder().key, key)
        self.assertEqual(person.to_builder().first_name, first_name)
        self.assertEqual(person.to_builder().last_name, last_name)
        self.assertEqual(person.to_builder().username, username)
        self.assertEqual(person.to_builder().phone_number, phone_number)
        self.assertEqual(person.to_builder().email, email)
