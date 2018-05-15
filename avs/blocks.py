from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class EventListBlock(blocks.StructBlock):
    """ Shows a list of upcoming events. """
    class Meta:
        icon = "fa-calendar"
        label = "Event List"
        help_text = "Displays a list of upcoming events."


class CtaBlock(blocks.StructBlock):
    """
    Directs users elsewhere by showing an image and some info with a button.
    """
    headline = blocks.CharBlock(
        max_length=100,
        help_text="A brief demand with a verb."
    )
    image = ImageChooserBlock(
        help_text="Upload an image to show alongside the call-to-action."
    )
    text = blocks.RichTextBlock(
        help_text="A description about why a user should click the button, "
                  "and what to expect when they do."
    )
    button_text = blocks.CharBlock(
        max_length=50,
        help_text="A verb for the user's action. 1-3 words."
    )
    button_url = blocks.URLBlock(
        label="Button URL",
        help_text="The target location of the button. ex. "
                  "https://americanvegan.org/my-page/"
    )

    class Meta:
        icon = "fa-crosshairs"
        label = "Call-to-Action"
        help_text = "Entices the viewer to click onto a different page."


class PortalListBlock(blocks.StructBlock):
    """
    Lists the portal pages with a call-to-action directing users where they
    want to go.
    """
    class Meta:
        icon = "fa-road"
        label = "Portal List"
        help_text = ("Displays a list of portal pages with their title and "
                     "image.")


class QuoteBlock(blocks.StructBlock):
    """ Share a quote and an image of the speaker. """
    title = blocks.CharBlock(
        max_length=100,
        help_text="Into text to this quote, including the name of the "
                  "speaker.",
        required=False
    )
    quote = blocks.RichTextBlock(
        features=['bold', 'italic'],
        help_text="The text of the quotation. Include the name of the speaker "
                  "if it's not in the title"
    )
    button_text = blocks.CharBlock(
        max_length=100,
        help_text="A verb for the user's action. Ex. Learn more about..."
    )
    button_url = blocks.URLBlock(
        label="Button URL",
        help_text="The target location of the button. ex. "
                  "https://americanvegan.org/my-page/"
    )
    image = ImageChooserBlock(
        help_text="Upload an image to show alongside the quote."
    )

    class Meta:
        icon = "fa-quote-left"
        label = "Quotation"
        help_text = "Displays a quotation and a picture"


class FeaturedPageBlock(blocks.StructBlock):
    headline = blocks.CharBlock(
        max_length=255,
        help_text="The header of this section",
        required=False,
    )
    text = blocks.RichTextBlock(
        help_text="A description of the section.",
        required=False,
    )
    pages = blocks.ListBlock(blocks.PageChooserBlock(
        help_text="Select the pages you would like to highlight"
    ))
    button_text = blocks.CharBlock(
        max_length=100,
        help_text="A verb for the user's action. Ex. Learn more about...",
        required=False,
    )
    button_url = blocks.URLBlock(
        label="Button URL",
        help_text="The target location of the button. ex. "
                  "https://americanvegan.org/my-page/",
        required=False,
    )

    class Meta:
        icon = "fa-file-o"
        label = "Featured Pages"
        help_text = "Displays 3 featured pages with their thumbnails and titles"


class MagazineListBlock(blocks.StructBlock):
    class Meta:
        icon = "fa-newspaper-o"
        help_text = "Displays images past magazines with links to view them"


class SectionBlock(blocks.StructBlock):
    headline = blocks.CharBlock(
        max_length=255,
        help_text="The header of this section",
        required=False,
    )
    text = blocks.RichTextBlock(
        help_text="A description of the section.",
        required=False,
    )

    class Meta:
        icon = "fa-puzzle-piece"
        label = "Section Block"
        help_text = "Displays long-form information to the reader."
