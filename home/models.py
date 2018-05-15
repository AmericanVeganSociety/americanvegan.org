from django.db import models
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from avs.blocks import (
    EventListBlock, CtaBlock, PortalListBlock, QuoteBlock,
    FeaturedPageBlock, MagazineListBlock
)


class HomePage(Page):
    """
    Main site landing page. Displays important news and updates and helps direct
    users towards information they may be looking for.
    """
    body = StreamField([
        ('events_list', EventListBlock()),
        ('cta', CtaBlock()),
        ('portal', PortalListBlock()),
        ('quote', QuoteBlock()),
        ('featured_pages', FeaturedPageBlock()),
        ('magazines', MagazineListBlock())
    ])
