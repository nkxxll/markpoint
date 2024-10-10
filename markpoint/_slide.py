from enum import Enum

__all__ = ["SlideInfo", "Text", "TextType"]


class TextType(Enum):
    Text = 1
    Bullet = 2


class Text:
    def __init__(self, text, level, type_) -> None:
        self._text = text
        self._level = level
        self._type = type_


class SlideInfo:
    def __init__(self, header, text) -> None:
        self.header = header
        self.text = text
