import logging

from ._slide import SlideInfo, Text, TextType

__all__ = ["MarkParser"]

logger = logging.getLogger(__name__)


class MarkParser:
    _LEVEL1 = " " * 2
    _LEVEL2 = " " * 4
    _STAR = "* "
    _HYPHEN = "- "
    _PLUS = "+ "

    def __init__(self, input: str) -> None:
        self._slides: list[SlideInfo] = self._parse(input)

    @staticmethod
    def _parse(input: str) -> list[SlideInfo]:
        lines = input.split("\n")
        header = ""
        text = []
        res = []
        for line in lines:
            if line.startswith("# "):
                if header != "":
                    res.append(SlideInfo(header, text.copy()))
                    header = ""
                    text = []
                header = line[2:]
            elif (
                line.startswith(MarkParser._HYPHEN)
                or line.startswith(MarkParser._STAR)
                or line.startswith(MarkParser._PLUS)
            ):
                text.append(Text(line[2:], 0, TextType.Bullet))
            elif (
                line.startswith(MarkParser._LEVEL1 + MarkParser._HYPHEN)
                or line.startswith(MarkParser._LEVEL1 + MarkParser._STAR)
                or line.startswith(MarkParser._LEVEL1 + MarkParser._PLUS)
            ):
                text.append(Text(line[4:], 1, TextType.Bullet))
            elif (
                line.startswith(MarkParser._LEVEL2 + MarkParser._HYPHEN)
                or line.startswith(MarkParser._LEVEL2 + MarkParser._STAR)
                or line.startswith(MarkParser._LEVEL2 + MarkParser._PLUS)
            ):
                text.append(Text(line[6:], 2, TextType.Bullet))
            elif line != "":
                text.append(Text(line, 0, TextType.Text))
        if header != "":
            res.append(SlideInfo(header, text))
        return res

    @property
    def slides(self) -> list[SlideInfo]:
        return self._slides
