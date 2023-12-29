import graphene
from graphene import ObjectType, Schema

from api.person_type.mutations.login import Login
from api.person_type.person_type import PersonType


class NotLoggedInException(Exception):
    pass


class PersonQuery(ObjectType):
    me = graphene.Field(PersonType, required=True)

    def resolve_me(self, info):
        user = info.context.user
        if not user:
            raise NotLoggedInException("User not logged in")

        return info.context.user.transform_to_immutable_entity().to_person_type()


class PersonMutation(graphene.ObjectType):
    login = Login.Field()


schema = Schema(query=PersonQuery, mutation=PersonMutation)
