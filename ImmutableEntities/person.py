from dataclasses import dataclass
from typing import Optional


# Immutable entity for Me
@dataclass(frozen=True)
class Person:
    key: str
    username: str
    first_name: str
    last_name: str
    email: str
    phone_number: str

    class PersonBuilder:
        key: Optional[str]
        username: Optional[str]
        first_name: Optional[str]
        last_name: Optional[str]
        email: Optional[str]
        phone_number: Optional[str]

        def __init__(self):
            self.key = None
            self.username = None
            self.first_name = None
            self.last_name = None
            self.email = None
            self.phone_number = None

        def set_key(self, key: str) -> "Person.PersonBuilder":
            self.key = key
            return self

        def set_username(self, username: str) -> "Person.PersonBuilder":
            self.username = username
            return self

        def set_first_name(self, first_name: str) -> "Person.PersonBuilder":
            self.first_name = first_name
            return self

        def set_last_name(self, last_name: str) -> "Person.PersonBuilder":
            self.last_name = last_name
            return self

        def set_email(self, email: str) -> "Person.PersonBuilder":
            self.email = email
            return self

        def set_phone_number(self, phone_number: str) -> "Person.PersonBuilder":
            self.phone_number = phone_number
            return self

        def build(self) -> "Person":
            assert self.key
            assert self.username
            assert self.first_name
            assert self.last_name
            assert self.email
            assert self.phone_number

            return Person(
                key=self.key,
                username=self.username,
                first_name=self.first_name,
                last_name=self.last_name,
                email=self.email,
                phone_number=self.phone_number,
            )

    def to_builder(self) -> PersonBuilder:
        return (
            self.PersonBuilder()
            .set_email(self.email)
            .set_username(self.username)
            .set_phone_number(self.phone_number)
            .set_first_name(self.first_name)
            .set_last_name(self.last_name)
        )
