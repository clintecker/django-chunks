# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Chunk(models.Model):
    """
    A Chunk is a piece of content associated
    with a unique key that can be inserted into
    any template with the use of a special template
    tag
    """
    key = models.CharField( _('Key'), help_text=_("A unique name for this chunk of content"), blank=False, max_length=255, unique=True)
    content = models.TextField( _('Content'),blank=True)
    description = models.TextField( _('Description'),blank=True, unique=False)

    def __unicode__(self):
        return u"%s" % (self.key,)

    class Meta:
        verbose_name = _('Chunk')
        verbose_name_plural = _('Chunks')
