import pytest
from datetime import datetime

from domain.values.messages import Text
from domain.entities.messages import Message

def test_create_message_success():
    text = Text(value='Hello')
    message = Message(text=text)
    
    assert message.text == text
    assert message.created_at.date() == datetime.today().date()