import pytest
from datetime import datetime

from domain.exceptions.messages import TextTooLongException
from domain.values.messages import Text, Title
from domain.entities.messages import Chat, Message


def test_create_message_success_short_text():
    text = Text(value="Hello")
    message = Message(text=text)

    assert message.text == text
    assert message.created_at.date() == datetime.today().date()


def test_create_message_success_long_text():

    text = Text("test" * 255)
    message = Message(text=text)

    assert message.text == text
    assert message.created_at.date() == datetime.today().date()


def test_create_chat_success():
    title = Title(value="Test")
    text = Text(value="Test")
    message = Message(text=text)
    chat = Chat(title=title)
    chat.add_message(message=message)

    assert chat.title == title
    assert message in chat.messages
    
