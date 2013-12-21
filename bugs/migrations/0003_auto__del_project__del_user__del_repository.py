# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'bugs_project')

        # Deleting model 'User'
        db.delete_table(u'bugs_user')

        # Deleting model 'Repository'
        db.delete_table(u'bugs_repository')


    def backwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'bugs_project', (
            ('wiki', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('maintainer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_in_maintainer_role', to=orm['bugs.User'])),
            ('repository', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bugs.Repository'])),
            ('download_page', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('documenter', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_in_documenter_role', to=orm['bugs.User'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('developer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_in_developer_role', to=orm['bugs.User'])),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('download_mirror', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('helper', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_in_helper_role', to=orm['bugs.User'])),
        ))
        db.send_create_signal(u'bugs', ['Project'])

        # Adding model 'User'
        db.create_table(u'bugs_user', (
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'bugs', ['User'])

        # Adding model 'Repository'
        db.create_table(u'bugs_repository', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'bugs', ['Repository'])


    models = {
        
    }

    complete_apps = ['bugs']