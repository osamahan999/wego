from graphene import ObjectType, Schema, String

from api.person_type.person_schema import PersonMutation, PersonQuery


class ExtendedQuery(PersonQuery):
    pass


class ExtendedMutation(PersonMutation):
    pass


class Query(ExtendedQuery, ObjectType):
    x = String()

    def resolve_x(self, info):
        return "hi!!!"


class Mutation(ExtendedMutation, ObjectType):
    pass


schema = Schema(query=Query, mutation=Mutation)
