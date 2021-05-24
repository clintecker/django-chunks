from django import template
from chunks.models import Chunk
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def chunk(key):
    try:
        return mark_safe(Chunk.objects.get(key=key).content)
    except:
        return ''


@register.simple_tag
def get_chunk(key):
    try:
        return Chunk.objects.get(key=key)
    except:
        return None
