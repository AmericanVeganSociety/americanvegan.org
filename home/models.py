from django.db import models
from wagtail.core.fields import StreamField
from wagtail.core import blocks

from wagtail.core.models import Page


class EventListBlock(blocks.StructBlock):
    """ Shows a list of upcoming events. """
    class Meta:
        icon = "fa-calendar"
        label = "Event List"
        help_text = "Displays a list of upcoming events."


class CtaBlock(blocks.StructBlock):
    """ Directs users elsewhere by showing a series of cards. """
    headline = blocks.CharBlock(
        max_length=100,
        help_text="A brief demand with a verb."
    )
    image = blocks.ImageChooserBlock(
        help_text="Upload an image to show alongside the call-to-action."
    )
    tagline = blocks.CharBlock(
        max_length=255,
        help_text="One sentence about what users can expect once they click "
                  "the button."
    )
    button_text = blocks.CharBlock(
        max_length=50,
        help_text="A verb for the user's action. 1-3 words."
    )
    button_url = blocks.UrlBlock(
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
        help_text = "Displays a list of portal pages with their title and "
                    "image."


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
    button_url = blocks.UrlBlock(
        label="Button URL",
        help_text="The target location of the button. ex. "
                  "https://americanvegan.org/my-page/"
    )
    image = blocks.ImageChooserBlock(
        help_text="Upload an image to show alongside the quote."
    )

    class Meta:
        icon = "fa-quote-left"
        label = "Quotation"
        help_text = "Displays a quotation and a picture"


class FeaturedPageBlock(blocks.StructBlock):
    pages = blocks.ListBlock(blocks.PageChooserBlock(
        help_text="Select the pages you would like to highlight"
    ))
    button_text = blocks.CharBlock(
        max_length=100,
        help_text="A verb for the user's action. Ex. Learn more about..."
    )
    button_url = blocks.UrlBlock(
        label="Button URL",
        help_text="The target location of the button. ex. "
                  "https://americanvegan.org/my-page/"
    )

    class Meta:
        icon = "fa-file-o"
        label = "Featured Pages"
        help_text = "Displays 3 featured pages with their thumbnails and titles"


class MagazineListBlock(blocks.StructBlock):
    class Meta:
        icon = "fa-newspaper-o"
        help_text = "Displays images past magazines with links to view them"


class HomePage(Page):
    """
    Main site landing page. Displays important news and updates and helps direct
    users towards information they may be looking for.
    """
    body = StreamField([
        ('events_list', EventListBlock()),
        ('cta', CtaBlock())
        ('portal', PortalListBlock()),
        ('quote', QuoteBlock()),
        ('featured_pages', FeaturedPageBlock()),
        ('magazines', MagazineListBlock())
    ])
