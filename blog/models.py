from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class BlogIndexPage(Page):
    """
    Shows a list of magazine articles published as a blog.
    """

    subpage_types = [
        'blog.BlogPage'
    ]


class BlogPage(Page):
    """
    Displays a magazine article republished online as a blog post, usually from the latest issue as a 'teaser'."
    """
    published_date = models.DateTimeField(
        help_text="Date this blog is published."
    )

    author = models.CharField(
        blank=True,
        max_length=100,
        help_text="Who wrote this article?"
    )

    body = RichTextField(
        help_text="Write the article here. Feel free to include any pictures or media throughout"
    )

    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
        blank=True,
        help_text="The default image associated with this blog post, may be used as a thumbnail. Avoid using images with text."
    )

    parent_page_types = [
        'blog.BlogIndexPage'
    ]

    content_panels = Page.content_panels + [
        FieldPanel('published_date'),
        FieldPanel('author'),
        FieldPanel('body'),
        FieldPanel('image'),
    ]
