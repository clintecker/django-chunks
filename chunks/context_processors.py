import json
from django.core.cache import cache
from django.utils.html import mark_safe
from .models import Chunk

CACHE_KEY = 'chunks'


def get_chunks_data():
    result = {}
    for chunk in Chunk.objects.all():
        result[chunk.key] = {
            'content': chunk.content,
            'file': chunk.file.url if chunk.file else None
        }
    return result


def chunks_processor(request):
    chunks_json = cache.get(CACHE_KEY)
    if chunks_json:
        raw_chunks = json.loads(chunks_json)
    else:
        raw_chunks = get_chunks_data()
        cache.set(CACHE_KEY, json.dumps(raw_chunks, ensure_ascii=False))

    chunks = {}
    for key, val in raw_chunks.iteritems():
        chunks[key] = {
            'content': mark_safe(val['content']),
            'file': val['file']
        }
    return {'chunks': chunks}
