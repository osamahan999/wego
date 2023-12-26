import graphene
from graphene import ObjectType, Schema

from api.person_type.mutations.login import Login
from api.person_type.person_type import PersonType
from result_querier.person_querier.person_querier import PersonQuerier


class PersonQuery(ObjectType):
    me = graphene.Field(PersonType, required=True)

    def resolve_me(self, info):
        return PersonType.get_person_type(
            PersonQuerier.transform_to_immutable_entity(info.context.user)
        )


class PersonMutation(graphene.ObjectType):
    login = Login.Field()


schema = Schema(query=PersonQuery, mutation=PersonMutation)
