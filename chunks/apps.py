from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ChunksAppConfig(AppConfig):
    name = 'chunks'
    verbose_name = _('Chunk')

    class Meta:
        app_label = 'chunks'

    def ready(self):
        from . import signals