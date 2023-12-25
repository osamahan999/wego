from dataclasses import dataclass
from typing import Optional


# Immutable entity for Chat
@dataclass(frozen=True)
class ImmutableChat:
    key: str
    message_text: str
    author_id: str

    class ImmutableChatBuilder:
        key: Optional[str]
        message_text: Optional[str]
        author_id: Optional[str]

        def __init__(self):
            self.key = None
            self.message_text = None
            self.author_id = None

        def set_key(self, key: str) -> "ImmutableChat.ImmutableChatBuilder":
            self.key = key
            return self

        def set_message_text(
            self, message_text: str
        ) -> "ImmutableChat.ImmutableChatBuilder":
            self.message_text = message_text
            return self

        def set_author_id(self, author_id: str) -> "ImmutableChat.ImmutableChatBuilder":
            self.author_id = author_id
            return self

        def build(self) -> "ImmutableChat":
            assert self.key
            assert self.message_text
            assert self.author_id

            return ImmutableChat(
                key=self.key,
                message_text=self.message_text,
                author_id=self.author_id,
            )

    def to_builder(self) -> ImmutableChatBuilder:
        return (
            self.ImmutableChatBuilder()
            .set_key(self.key)
            .set_message_text(self.message_text)
            .set_author_id(self.author_id)
        )
