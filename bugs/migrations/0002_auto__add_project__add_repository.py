# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'bugs_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('developer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_in_developer_role', to=orm['bugs.User'])),
            ('documenter', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_in_documenter_role', to=orm['bugs.User'])),
            ('maintainer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_in_maintainer_role', to=orm['bugs.User'])),
            ('helper', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_in_helper_role', to=orm['bugs.User'])),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('download_mirror', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('download_page', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('repository', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bugs.Repository'])),
            ('wiki', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'bugs', ['Project'])

        # Adding model 'Repository'
        db.create_table(u'bugs_repository', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'bugs', ['Repository'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'bugs_project')

        # Deleting model 'Repository'
        db.delete_table(u'bugs_repository')


    models = {
        u'bugs.project': {
            'Meta': {'object_name': 'Project'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'developer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_in_developer_role'", 'to': u"orm['bugs.User']"}),
            'documenter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_in_documenter_role'", 'to': u"orm['bugs.User']"}),
            'download_mirror': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'download_page': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'helper': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_in_helper_role'", 'to': u"orm['bugs.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maintainer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_in_maintainer_role'", 'to': u"orm['bugs.User']"}),
            'repository': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bugs.Repository']"}),
            'wiki': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'bugs.repository': {
            'Meta': {'object_name': 'Repository'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'bugs.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bugs']