from django.db.models.signals import post_save, post_delete
from django.core.cache import cache
from .models import Chunk


def chunks_change_handler(sender, instance, **kwargs):
    cache.delete('chunks')


post_save.connect(chunks_change_handler, Chunk)
post_delete.connect(chunks_change_handler, Chunk)

