from django.contrib import admin
from models import Chunk

class ChunkAdmin(admin.ModelAdmin):
  list_display = ('key', 'description')
  search_fields = ('key', 'content')

admin.site.register(Chunk, ChunkAdmin)
