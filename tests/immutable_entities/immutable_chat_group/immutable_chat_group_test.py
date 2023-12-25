from unittest import TestCase

from immutable_entities.immutable_chat import ImmutableChat
from immutable_entities.immutable_chat_group import ImmutableChatGroup


class ImmutableChatGroupTest(TestCase):
    def test_immutable_chat_group_builder(self):
        key: int = "0"
        messages: list[ImmutableChat] = [
            ImmutableChat.ImmutableChatBuilder()
            .set_key(1)
            .set_message_text("message1")
            .set_author_id("author_1")
            .build(),
            ImmutableChat.ImmutableChatBuilder()
            .set_key(2)
            .set_message_text("message2")
            .set_author_id("author_2")
            .build(),
            ImmutableChat.ImmutableChatBuilder()
            .set_key(3)
            .set_message_text("message3")
            .set_author_id("author_1")
            .build(),
        ]

        # Assert that ImmutableChatGroup constructor works
        self.assertIsNotNone(ImmutableChatGroup.ImmutableChatGroupBuilder())
        self.assertIsInstance(
            ImmutableChatGroup.ImmutableChatGroupBuilder(),
            ImmutableChatGroup.ImmutableChatGroupBuilder,
        )

        # Assert that ImmutableChatGroupBuilder.build
        chat_group: ImmutableChatGroup = (
            ImmutableChatGroup.ImmutableChatGroupBuilder()
            .set_key(key)
            .set_messages(messages)
            .build()
        )

        # assert data integrity from builder to class
        self.assertIsNotNone(chat_group)
        self.assertEqual(chat_group.key, key)
        self.assertEqual(chat_group.messages, frozenset(messages))

        # to_builder
        self.assertIsInstance(
            chat_group.to_builder(), ImmutableChatGroup.ImmutableChatGroupBuilder
        )

        # Assert data integrity from class to builder
        self.assertEqual(chat_group.to_builder().key, key)
        self.assertEqual(set(chat_group.to_builder().messages), set(messages))
