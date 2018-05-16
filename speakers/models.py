from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from phonenumber_field.modelfields import PhoneNumberField


class SpeakerIndexPage(Page):
    """
    Shows a list of Speakers Bureau members.
    """

    subpage_types = [
        'speakers.SpeakerPage'
    ]


class SpeakerPage(Page):
    """
    Displays information about individual speakers.
    """

    name = models.CharField(
        max_length=100,
        blank=True,
        help_text="Name and titles of speaker, ex. Maria Sand, MSW, LSC, FBI"
    )

    state = models.CharField(
        max_length=100,
        blank=True,
        help_text="ex. PA"
    )

    talks = RichTextField(
        blank=True,
        help_text="A sample of talks the speaker may provide, ex. Eating for Cancer Survival"
        )

    website = models.URLField(
        blank=True,
        help_text="The speaker's personal or professional website"
    )

    email = models.EmailField(
        blank=True,
        help_text="An email by which the speaker may be contacted"
    )

    phone = PhoneNumberField(
        blank=True,
        help_text="A phone number by which the speaker may be contacted"
    )

    bio = RichTextField(
        blank=True,
        help_text="describe the event"
        )

    headshot = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
        blank=True,
        help_text="A nice headshot of the speaker"
    )

    parent_page_types = [
        'speakers.SpeakerIndexPage'
    ]

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('state'),
        FieldPanel('talks'),
        FieldPanel('website'),
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('bio'),
        FieldPanel('headshot'),
    ]
