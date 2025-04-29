from .base import ApplicationException
from dataclasses import dataclass


@dataclass
class TextTooLongException(ApplicationException):
    text: str
    
    @property
    def message(self):
        return f'Text too long: {self.text}'

@dataclass
class EmptyTextException(ApplicationException):
    @property
    def message(self):
        return 'Text is empty'