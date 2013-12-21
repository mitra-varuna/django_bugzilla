# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'BugModel'
        db.delete_table(u'bugs_bugmodel')

        # Adding model 'Post'
        db.create_table(u'bugs_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='posts', to=orm['bugs.User'])),
            ('when', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('content', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bugs.Content'], unique=True)),
        ))
        db.send_create_signal('bugs', ['Post'])

        # Adding model 'Content'
        db.create_table(u'bugs_content', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('src', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('bugs', ['Content'])

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
        db.send_create_signal('bugs', ['Project'])

        # Adding model 'Priority'
        db.create_table(u'bugs_priority', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('bugs', ['Priority'])

        # Adding model 'User'
        db.create_table(u'bugs_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('bugs', ['User'])

        # Adding model 'Repository'
        db.create_table(u'bugs_repository', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('bugs', ['Repository'])


    def backwards(self, orm):
        # Adding model 'BugModel'
        db.create_table(u'bugs_bugmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('bugs', ['BugModel'])

        # Deleting model 'Post'
        db.delete_table(u'bugs_post')

        # Deleting model 'Content'
        db.delete_table(u'bugs_content')

        # Deleting model 'Project'
        db.delete_table(u'bugs_project')

        # Deleting model 'Priority'
        db.delete_table(u'bugs_priority')

        # Deleting model 'User'
        db.delete_table(u'bugs_user')

        # Deleting model 'Repository'
        db.delete_table(u'bugs_repository')


    models = {
        'bugs.content': {
            'Meta': {'object_name': 'Content'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'src': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'bugs.post': {
            'Meta': {'object_name': 'Post'},
            'content': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bugs.Content']", 'unique': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': "orm['bugs.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'when': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'bugs.priority': {
            'Meta': {'object_name': 'Priority'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'bugs.project': {
            'Meta': {'object_name': 'Project'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'developer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_in_developer_role'", 'to': "orm['bugs.User']"}),
            'documenter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_in_documenter_role'", 'to': "orm['bugs.User']"}),
            'download_mirror': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'download_page': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'helper': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_in_helper_role'", 'to': "orm['bugs.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maintainer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_in_maintainer_role'", 'to': "orm['bugs.User']"}),
            'repository': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bugs.Repository']"}),
            'wiki': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'bugs.repository': {
            'Meta': {'object_name': 'Repository'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'bugs.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bugs']