# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Chunk.description'
        db.alter_column('chunks_chunk', 'description', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # Changing field 'Chunk.description'
        db.alter_column('chunks_chunk', 'description', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        'chunks.chunk': {
            'Meta': {'object_name': 'Chunk'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['chunks']