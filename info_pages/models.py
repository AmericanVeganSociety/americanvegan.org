from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from avs.blocks import (
    EventListBlock, CtaBlock, QuoteBlock,
    FeaturedPageBlock, MagazineListBlock, SectionBlock
)
from wagtail.images.edit_handlers import ImageChooserPanel



class InfoPage(Page):
    """
    A child page of a portal which displays long-form information to a curious
    reader, usually limited to a specific topic, ex. "About Ahimsa"
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
        ('magazines', MagazineListBlock()),
        ('section_block', SectionBlock())
    ])

    parent_page_types = [
        'portals.PortalPage'
    ]

    # TODO: sidebar = sidebar ???

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        ImageChooserPanel('listing_image'),
    ]
