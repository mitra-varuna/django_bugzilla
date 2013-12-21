# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BugModel'
        db.create_table(u'bugs_bugmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('bugs', ['BugModel'])


    def backwards(self, orm):
        # Deleting model 'BugModel'
        db.delete_table(u'bugs_bugmodel')


    models = {
        'bugs.bugmodel': {
            'Meta': {'object_name': 'BugModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['bugs']