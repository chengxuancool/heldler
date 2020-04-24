from django.template import Library
from core.models.entry import Entry

register = Library()

@register.inclusion_tag('core/tags/swap.html')
def get_featured_entries(number=5, template='core/tags/content.html'):
    """
    Return the featured entries.
    """
    return {'template': template,
            'content': Entry.published.all()[:number]}