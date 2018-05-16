from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from phonenumber_field.modelfields import PhoneNumberField



class VIPPage(Page):
    """
    Displays vegan information points.
    """

class VIPs(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="What is the name of the VIP?"
    )
    address_name = models.CharField(
        max_length=100,
        blank=True,
        help_text="Ex. Ithaca College"
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
    phone_number = PhoneNumberField(
        max_length=100,
        blank=True,
        help_text="ex. 234-567-9895"
    )
    email = models.CharField(
        max_length=100,
        blank=True,
        help_text="ex. jane@smith.edu"
    )
    details = RichTextField(
        blank=True,
        help_text="Any details you would like to share about this person?"
    )

    #TODO: How are these VIPs being edited by the admin and shown on the page?
