from unittest import TestCase

from immutable_entities.immutable_chat import ImmutableChat


class ImmutableChatTest(TestCase):
    def test_immutable_chat_builder(self):
        key: int = 1
        message_text: str = "message_text"
        author_id: int = 1

        # Assert that ImmutableChatBuilder constructor works
        self.assertIsNotNone(ImmutableChat.ImmutableChatBuilder())
        self.assertIsInstance(
            ImmutableChat.ImmutableChatBuilder(),
            ImmutableChat.ImmutableChatBuilder,
        )

        # Assert that ImmutableChat.build
        chat: ImmutableChat = (
            ImmutableChat.ImmutableChatBuilder()
            .set_key(key)
            .set_message_text(message_text)
            .set_author_id(author_id)
            .build()
        )

        # assert data integrity from builder to class
        self.assertIsNotNone(chat)
        self.assertEqual(chat.key, key)
        self.assertEqual(chat.message_text, message_text)
        self.assertEqual(chat.author_id, author_id)

        # to_builder
        self.assertIsInstance(chat.to_builder(), ImmutableChat.ImmutableChatBuilder)

        # Assert data integrity from class to builder
        self.assertEqual(chat.to_builder().key, key)
        self.assertEqual(chat.to_builder().message_text, message_text)
        self.assertEqual(chat.to_builder().author_id, author_id)
