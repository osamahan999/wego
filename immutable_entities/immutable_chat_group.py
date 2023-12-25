from dataclasses import dataclass
from typing import Optional

from immutable_entities.immutable_chat import ImmutableChat


# Immutable entity for ChatGroup
@dataclass(frozen=True)
class ImmutableChatGroup:
    key: str
    messages: frozenset[ImmutableChat]

    class ImmutableChatGroupBuilder:
        key: Optional[str]
        messages: list[ImmutableChat]

        def __init__(self):
            self.key = None
            self.messages = []

        def set_key(self, key: str) -> "ImmutableChatGroup.ImmutableChatGroupBuilder":
            self.key = key
            return self

        def set_messages(
            self, messages: list[ImmutableChat]
        ) -> "ImmutableChatGroup.ImmutableChatGroupBuilder":
            self.messages = messages
            return self

        def build(self) -> "ImmutableChatGroup":
            assert self.key
            assert self.messages

            return ImmutableChatGroup(
                key=self.key,
                messages=frozenset(self.messages),
            )

    def to_builder(self) -> ImmutableChatGroupBuilder:
        return (
            self.ImmutableChatGroupBuilder()
            .set_key(self.key)
            .set_messages(list(self.messages))
        )
