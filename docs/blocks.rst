======
Blocks
======

americanvegan.org uses Wagtail's `StreamField <https://wagtail.io/features/streamfield/>`_ to organize page content.
StreamField breaks up the page in terms of *blocks*.
A block is a UI element which serves a specific purpose.
Usually a block takes up an entire horizontal row of the page.
Blocks of the same time will often look the same across pages, but they can also change appearance based on their context.

General
=======
These blocks can be created in multiple, unrelated sections of the website.

Event List
~~~~~~~~~~
.. class:: avs.blocks.EventListBlock

This placeholder block has no fields.
It renders mini event boxes that take users to the event page when clicked.
Events are upcoming and in reverse-cronological order.

Call-to-Action
~~~~~~~~~~~~~~
.. class:: avs.blocks.CtaBlock

    Renders a callout with an optional image and a clickable button.
    The goal is to encourage the user to visit another web page.

    .. attribute:: headline

      **text** ---
      A brief demand with a verb.
      *Ex. "Become a member today!"*

    .. attribute:: image

      **image** *(optional)* ---
      Ideally, an illustration of the action the user should take.
      Could be a photo or a drawing.
      Should have a transparent background.

    .. attribute:: text

      **text** ---
      An explanation for why the user should click the button, and what to expect when they do.
      *Ex. "Becoming a member will let you support an important cause. Sign up now!"*

    .. attribute:: button_text

      **text** ---
      A verb for the user's action in 1--3 words.
      *Ex. "Sign up"*

    .. attribute:: button_url

      **URL** ---
      The URL the button will take the user.
      *Ex.* ``https://americanvegan.org/my-page/``


TODO: Add more!
