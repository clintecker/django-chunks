from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from .models import Chunk


class ChunkAdmin(admin.ModelAdmin):

    def get_content(self, obj):
        return obj.content[0:50]

    get_content.short_description = _('content')
    list_display = ('key', 'description', 'get_content')
    search_fields = ('key', 'content')


admin.site.register(Chunk, ChunkAdmin)
