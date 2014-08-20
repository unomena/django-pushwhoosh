# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PushWhooshNotification.response_data'
        db.add_column('pushwhoosh_pushwhooshnotification', 'response_data',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'PushWhooshNotification.request_data'
        db.alter_column('pushwhoosh_pushwhooshnotification', 'request_data', self.gf('django.db.models.fields.TextField')(default=''))

    def backwards(self, orm):
        # Deleting field 'PushWhooshNotification.response_data'
        db.delete_column('pushwhoosh_pushwhooshnotification', 'response_data')


        # Changing field 'PushWhooshNotification.request_data'
        db.alter_column('pushwhoosh_pushwhooshnotification', 'request_data', self.gf('django.db.models.fields.TextField')(null=True))

    models = {
        'pushwhoosh.pushwhooshnotification': {
            'Meta': {'object_name': 'PushWhooshNotification'},
            'api_method': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request_data': ('django.db.models.fields.TextField', [], {}),
            'response_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['pushwhoosh']