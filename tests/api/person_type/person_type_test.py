from django.test import Client as DjangoTestClient, RequestFactory, TransactionTestCase
from graphene.test import Client as GrapheneClient

from api.person_type.person_type import PersonType
from api.schema import schema
from immutable_entities.immutable_event import immutable_event
from immutable_entities.immutable_person import ImmutablePerson
from person.models import Person
from tests.seeder import Seeder


class PersonTypeTest(TransactionTestCase):
    USERNAME: str = "osama"
    PASSWORD: str = "osama"
    EMAIL: str = "osama@gmail.com"

    client: DjangoTestClient = None
    graphql_client: GrapheneClient = None
    user: Person = None

    def setUp(self) -> None:
        self.client = DjangoTestClient()
        self.user = Person.objects.create_user(
            username=self.USERNAME, password=self.PASSWORD, email=self.PASSWORD
        )

        self.client.login(username=self.USERNAME, password=self.PASSWORD)

        request_factory = RequestFactory()
        request = request_factory.post("/graphql/")
        request.user = self.user

        self.graphql_client = GrapheneClient(schema, context=request)

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

        self.assertEqual(person.to_person_type(), expected_person_type)

    def test_get_me(self):
        query: str = """
            query {
                me {
                    id,
                    username,
                    firstName,
                    lastName,
                    email,
                    phoneNumber
                }
            }
        """
        result = self.graphql_client.execute(query)

        assert not result.get("errors")

        self.assertEqual(result.get("data").get("me").get("username"), self.USERNAME)
        self.assertEqual(result.get("data").get("me").get("firstName"), "")

    def test_get_owned_events(self):
        events = Seeder.seed_events(
            [
                immutable_event.ImmutableEvent.ImmutableEventBuilder()
                .set_owner(self.user.transform_to_immutable_entity())
                .set_name("name")
                .set_description("description")
                .set_location("location")
                .set_latitude(3.0)
                .set_longitude(4.0)
                .set_attendees([self.user.transform_to_immutable_entity()])
                .build(),
                immutable_event.ImmutableEvent.ImmutableEventBuilder()
                .set_owner(self.user.transform_to_immutable_entity())
                .set_name("name2")
                .set_description("description2")
                .set_location("location2")
                .set_latitude(3.0)
                .set_longitude(4.0)
                .set_attendees([self.user.transform_to_immutable_entity()])
                .build(),
            ]
        )

        query: str = """
            query {
                me {
                    id,
                    ownedEvents {
                        edges {
                            node {
                                id,
                                name
                            }
                        }
                    }
                }
            }
        """

        result = self.graphql_client.execute(query)

        self.assertIsNone(result.get("errors"))
        self.assertEqual(result.get("data").get("me").get("id"), self.user.id)

        nodes = [
            result.get("node")
            for result in result.get("data").get("me").get("ownedEvents").get("edges")
        ]
        event_1 = [node for node in nodes if node.get("name") == events[0].name][0]
        event_2 = [node for node in nodes if node.get("name") == events[1].name][0]

        self.assertIsNotNone(event_1)
        self.assertIsNotNone(event_2)
