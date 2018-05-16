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
    prep_time = models.CharField(max_length=100, blank=True)
    cook_time = models.CharField(max_length=100, blank=True)
    servings = models.CharField(max_length=100, blank=True)
    ingredients = RichTextField(blank=True)
    directions = RichTextField(blank=True)

    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
        blank=True
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
