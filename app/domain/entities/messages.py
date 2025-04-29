from dataclasses import dataclass, field

from domain.entities.base import BaseEntity
from domain.values.messages import Text, Title


@dataclass(eq=False)
class Message(BaseEntity):
    text: Text


@dataclass
class Chat:
    title: Title
    messages: set[Message] = field(default_factory=set, kw_only=True)
