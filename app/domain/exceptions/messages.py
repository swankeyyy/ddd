from .base import ApplicationException
from dataclasses import dataclass


@dataclass(eq=False)
class TextTooLongException(ApplicationException):
    text: str
    
    @property
    def message(self):
        return f'Text too long: {self.text}'

@dataclass(eq=False)
class EmptyTextException(ApplicationException):
    @property
    def message(self):
        return 'Text is empty'