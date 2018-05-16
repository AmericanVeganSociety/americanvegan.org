from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class RecipeIndexPage(Page):
    """
    Shows a list of vegan recipes.
    """

    subpage_types = [
        'recipes.RecipePage'
    ]


class RecipePage(Page):
    """
    Displays a vegan recipe.
    """
    prep_time = models.CharField(
        max_length=100,
        blank=True,
        help_text="How long will it take to prepare the ingredients?"
    )
    cook_time = models.CharField(
        max_length=100,
        blank=True,
        help_text="How much oven or stove time is involved?"
    )
    servings = models.CharField(
        max_length=100,
        blank=True,
        help_text="How many humans can this recipe serve?"
    )
    ingredients = RichTextField(
        blank=True,
        help_text="List the ingredients, and their amounts."
    )
    directions = RichTextField(
        blank=True,
        help_text="Describe the steps to this recipe in detail."
    )

    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
        blank=True,
        help_text="A mouth-watering picture of the recipe."
    )

    parent_page_types = [
        'recipes.RecipeIndexPage'
    ]

    content_panels = Page.content_panels + [
        FieldPanel('prep_time'),
        FieldPanel('cook_time'),
        FieldPanel('servings'),
        FieldPanel('ingredients'),
        FieldPanel('directions'),
        FieldPanel('image'),
    ]
