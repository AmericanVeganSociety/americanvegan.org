from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from avs.blocks import (
    EventListBlock, CtaBlock, QuoteBlock,
    FeaturedPageBlock, MagazineListBlock
)
from wagtail.images.edit_handlers import ImageChooserPanel


class PortalPage(Page):
    """
    A top-level navigation page. Displays select child pages, important info
    within the section, and helps direct users toward what they are looking
    for.
    """

    listing_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    body = StreamField([
        ('events_list', EventListBlock()),
        ('cta', CtaBlock()),
        ('quote', QuoteBlock()),
        ('featured_pages', FeaturedPageBlock()),
        ('magazines', MagazineListBlock())
    ])

    parent_page_types = [
        'home.HomePage'
    ]

    # TODO: sidebar = sidebar ???

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        ImageChooserPanel('listing_image'),
    ]
