from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel



class EventIndexPage(Page):
    """
    Shows a list of upcoming events.
    """

    subpage_types = [
        'events.EventPage'
    ]


class EventPage(Page):
    """
    Displays event information.
    """
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    address_name = models.CharField(
        max_length=100,
        blank=True,
        help_text="Ex. John's Pizzeria"
    )
    address_street = models.CharField(
        max_length=100,
        blank=True,
        help_text="ex. 123 E South St."
        )
    address_city = models.CharField(
        max_length=100,
        blank=True,
        help_text="ex. Philadelphia"
    )
    address_state = models.CharField(
        max_length=100,
        blank=True,
        help_text="ex. PA"
    )
    address_zip = models.CharField(
        max_length=100,
        blank=True,
        help_text="ex. 19140"
    )

    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
        blank=True,
        help_text="An attractive image that represents the event. Avoid images with text."
    )

    description = RichTextField(
        blank=True,
        help_text="describe the event"
        )

    type = models.CharField(
        max_length=100,
        choices=(
            ('AVS', 'AVS'),
            ('Other', 'Other'),
        ),
        help_text="Is this an official AVS event?"
    )

    parent_page_types = [
        'events.EventIndexPage'
    ]

    content_panels = Page.content_panels + [
        FieldPanel('start_time'),
        FieldPanel('end_time'),
        FieldPanel('address_name'),
        FieldPanel('address_street'),
        FieldPanel('address_city'),
        FieldPanel('address_state'),
        FieldPanel('address_zip'),
        ImageChooserPanel('image'),
        FieldPanel('description'),
        FieldPanel('type'),
    ]
