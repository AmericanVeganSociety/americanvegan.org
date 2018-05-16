from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class MagazineIndexPage(Page):
    """
    Shows a list of AVS magazines.
    """

    subpage_types = [
        'magazine.MagazinePage'
    ]


class MagazinePage(Page):
    """
    Allows the reader to browse an AVS magazine.
    """
    published_date = models.DateField(
        blank=True,
        help_text="Date this issue was originally published."
    )

    file = models.ForeignKey(
        'wagtaildocs.Document',
        on_delete=models.PROTECT,
        help_text="PDF version of this issue."
    )

    # TODO: generate image thumbnails from first page of PDF file?

    description = RichTextField(
        blank=True,
        help_text="Additional information about this issue."
    )

    public = models.BooleanField(
        default=False,
        help_text="By default, the PDF version is available to members only. "
                  "Enable this to allow anyone to download the PDF."
    )

    # TODO: automatically set public=True after next magazine is released?

    parent_page_types = [
        'magazine.MagazineIndexPage'
    ]

    content_panels = Page.content_panels + [
        FieldPanel('published_date'),
        FieldPanel('file'),
        FieldPanel('description'),
        FieldPanel('public'),
    ]
