import graphene
from django.contrib.auth import authenticate, login

from api.person_type.person_type import PersonType
from result_querier.person_querier.person_querier import PersonQuerier


class LoginSuccess(graphene.ObjectType):
    me = graphene.Field(PersonType, required=True)

    def __init__(self, me: PersonType):
        self.me = me


class LoginError(graphene.ObjectType):
    message = graphene.String(required=True)

    def __init__(self, message: str):
        self.message = message


class LoginPayload(graphene.Union):
    class Meta:
        types = (LoginSuccess, LoginError)


class Login(graphene.Mutation):
    Output = graphene.NonNull(LoginPayload)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, password):
        user = authenticate(username=username, password=password)
        if not user:
            return LoginError("Failed to authenticate user.")

        login(info.context, user)

        me: PersonType = PersonQuerier.get_immutable_person(user.id).to_person_type()

        return LoginSuccess(me)
