from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from avs.blocks import (
    EventListBlock, CtaBlock, QuoteBlock,
    FeaturedPageBlock, MagazineListBlock, SectionBlock
)


class InfoPage(Page):
    """
    A child page of a portal which displays long-form information to a curious reader, usually limited to a specific topic, ex. "About Ahimsa"
    """
    body = StreamField([
        ('events_list', EventListBlock()),
        ('cta', CtaBlock()),
        ('quote', QuoteBlock()),
        ('featured_pages', FeaturedPageBlock()),
        ('magazines', MagazineListBlock()),
        ('section_block', SectionBlock())
    ])

    # TODO: sidebar = sidebar ???

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
