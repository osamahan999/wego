from graphene import ObjectType, Schema, String


class Query(ObjectType):
    me = String()

    def resolve_me(self, info):
        return "hi"


schema = Schema(query=Query)
