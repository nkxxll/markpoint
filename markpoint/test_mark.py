from markpoint import MarkParser


def test_slideinfo(snapshot):
    text = """# header

- bullet
- bullet
- bullet
"""
    mp = MarkParser(text)
    res = "\n\n".join([repr(slide) for slide in mp.slides])
    snapshot.assert_match(res, "markparse_test.txt")
