from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from avs.blocks import (
    EventListBlock, CtaBlock, QuoteBlock,
    FeaturedPageBlock, MagazineListBlock
)


class PortalPage(Page):
    """
    A top-level navigation page. Displays select child pages, important info
    within the section, and helps direct users toward what they are looking
    for.
    """
    body = StreamField([
        ('events_list', EventListBlock()),
        ('cta', CtaBlock()),
        ('quote', QuoteBlock()),
        ('featured_pages', FeaturedPageBlock()),
        ('magazines', MagazineListBlock())
    ])

    # TODO: sidebar = sidebar ???

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
