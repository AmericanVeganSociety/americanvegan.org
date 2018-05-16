from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class MagazineIndexPage(Page):
    """
    Shows a list of AVS magazine.
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

    description = RichTextField(
        blank=True,
        help_text="Additional information about this issue."
    )

    public = models.BooleanField(
        default=False,
        help_text="By default, the PDF version is available to members only. "
                  "Enable this to allow anyone to download the PDF."
    )
