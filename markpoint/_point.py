from pptx import Presentation

from ._slide import SlideInfo

__all__ = ["PointGenerator"]


class PointGenerator:
    def __init__(self, slideinfo: list[SlideInfo] = []) -> None:
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

        # Add a blank slide layout
        slide_layout = prs.slide_layouts[1]  # Title and Content layout
        slide = prs.slides.add_slide(slide_layout)

        # Set the title
        title = slide.shapes.title
        title.text = "My Slide Title"

        # Add bullet points to the content placeholder
        print(slide.placeholders[1].shape_type)
        content = slide.placeholders[1]
        content.text = "This is some full text\nwith a new line and some other text that is really really long and so on and this text goes on and on it is so long it is very long long aber ich will nicht dass das Ganz zu lang wird aber schon ein bisschen laenger aber die Flughanfen Genoicde"

        # # Add bullet points as paragraphs
        # bullet_points = [
        #     "First bullet point",
        #     "Second bullet point",
        #     "Third bullet point",
        # ]
        # for point in bullet_points:
        #     p = content.text_frame.add_paragraph()
        #     p.text = point
        #     p.level = 1  # Indentation level (0 = main bullet, 1 = sub-bullet)

        # TODO: make all the checks for the outfile or create it or so
        # Save the presentation
        prs.save(outfile)
