from graphene import ObjectType, Schema

from api.person_type.person_schema import PersonMutation, PersonQuery


class ExtendedQuery(PersonQuery):
    pass


class ExtendedMutation(PersonMutation):
    pass


class Query(ExtendedQuery, ObjectType):
    pass


class Mutation(ExtendedMutation, ObjectType):
    pass


schema = Schema(query=Query, mutation=Mutation)
