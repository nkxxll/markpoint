from enum import Enum

__all__ = ["SlideInfo", "Text", "TextType"]


class TextType(Enum):
    Text = 1
    Bullet = 2


class Text:
    def __init__(self, text, level, type_) -> None:
        self._text = text
        self._level: int = level
        self._type = type_

    def __repr__(self) -> str:
        return f"<Level: {self._level}; Type: {repr(self._type)}; Text: {self._text}>"

    @property
    def text(self) -> str:
        return self._text

    @property
    def level(self) -> int:
        return self._level

    @property
    def type_(self) -> TextType:
        return self._type


class SlideInfo:
    def __init__(self, header: str, texts: list[Text]) -> None:
        self.header: str = header
        self.texts: list[Text] = texts

    def __str__(self) -> str:
        text = "\n".join(
            ["  " * (text.level) + "- " + text.text for text in self.texts]
        )
        string = f"{self.header}\n\n{text}"
        return string

    def __repr__(self) -> str:
        repres = f"Header: {self.header}\n"
        for text in self.texts:
            repres += repr(text) + "\n"
        return repres
