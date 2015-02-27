# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'app_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'app', ['Category'])

        # Adding model 'Element'
        db.create_table(u'app_element', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('css_string', self.gf('django.db.models.fields.CharField')(max_length=5000)),
            ('search_words', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['app.Category'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal(u'app', ['Element'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'app_category')

        # Deleting model 'Element'
        db.delete_table(u'app_element')


    models = {
        u'app.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'app.element': {
            'Meta': {'object_name': 'Element'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['app.Category']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'css_string': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'search_words': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        }
    }

    complete_apps = ['app']