from django import template
from events.models import EventPage

register = template.Library()

@register.simple_tag
def upcoming_events():
    events = EventPage.objects.live()
    return events
