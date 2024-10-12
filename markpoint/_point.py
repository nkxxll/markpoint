from pptx import Presentation

from ._slide import SlideInfo

__all__ = ["PointGenerator"]


class PointGenerator:
    def __init__(self, slideinfo: list[SlideInfo]) -> None:
        self._slideinfolist = slideinfo

    @property
    def slideinfo_list(self):
        return self._slideinfolist

    def generate(self, outfile: str) -> None:
        """generate powerpoint presentation

        Args:
            outfile: file to save the powerpoint presentation at
        """
        # Create a presentation object
        prs = Presentation()

        for s in self._slideinfolist:
            # Add a blank slide layout
            slide_layout = prs.slide_layouts[1]  # Title and Content layout
            slide = prs.slides.add_slide(slide_layout)

            # Set the title
            title = slide.shapes.title
            title.text = s.header

            # Add bullet points to the content placeholder
            content = slide.placeholders[1]
            for t in s.texts:
                p = content.text_frame.add_paragraph()
                p.text = t.text
                p.level = t.level
        prs.save(outfile)
