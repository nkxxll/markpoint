from ._slide import SlideInfo, Text, TextType

__all__ = ["MarkParser"]


class MarkParser:
    _LEVEL1 = " " * 2
    _LEVEL2 = " " * 4
    _STAR = "* "
    _HYPHEN = "- "
    _PLUS = "+ "

    def __init__(self, input: str) -> None:
        self._slide: list[SlideInfo] = self._parse(input)

    @staticmethod
    def _parse(input: str) -> list[SlideInfo]:
        lines = input.split("\n")
        header = ""
        text = ""
        res = []
        for line in lines:
            if line.startswith("# "):
                if header != "":
                    res.append(SlideInfo(header, text))
                    header = ""
                    text = ""
                header = line[2:]
            if (
                line.startswith(MarkParser._HYPHEN)
                or line.startswith(MarkParser._STAR)
                or line.startswith(MarkParser._PLUS)
            ):
                text = Text(line[2:], 0, TextType.Bullet)
            if (
                line.startswith(MarkParser._LEVEL1 + MarkParser._HYPHEN)
                or line.startswith(MarkParser._LEVEL1 + MarkParser._STAR)
                or line.startswith(MarkParser._LEVEL1 + MarkParser._PLUS)
            ):
                text = Text(line[4:], 1, TextType.Bullet)
            if (
                line.startswith(MarkParser._LEVEL2 + MarkParser._HYPHEN)
                or line.startswith(MarkParser._LEVEL2 + MarkParser._STAR)
                or line.startswith(MarkParser._LEVEL2 + MarkParser._PLUS)
            ):
                text = Text(line[6:], 2, TextType.Bullet)
            if line != "":
                text = Text(line, 0, TextType.Text)
        return res

    @property
    def slide(self) -> list[SlideInfo]:
        return self._slide
