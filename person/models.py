from __future__ import annotations

from django.contrib.auth.models import AbstractUser
from django.db import models

from immutable_entities.immutable_person import immutable_person


class Person(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def transform_to_immutable_entity(self) -> immutable_person.ImmutablePerson:
        person_builder: immutable_person.ImmutablePerson.ImmutablePersonBuilder = (
            immutable_person.ImmutablePerson.ImmutablePersonBuilder()
        )

        return (
            person_builder.set_key(self.id)
            .set_email(self.email)
            .set_username(self.username)
            .set_phone_number(self.phone_number)
            .set_first_name(self.first_name)
            .set_last_name(self.last_name)
            .build()
        )
