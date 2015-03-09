# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Publication'
        db.create_table('lineads_publication', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('job_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('lineads', ['Publication'])

        # Adding model 'Listing'
        db.create_table('lineads_listing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publication', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lineads.Publication'])),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('organization_name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('lineads', ['Listing'])


    def backwards(self, orm):
        
        # Deleting model 'Publication'
        db.delete_table('lineads_publication')

        # Deleting model 'Listing'
        db.delete_table('lineads_listing')


    models = {
        'lineads.listing': {
            'Meta': {'ordering': "('organization_name',)", 'object_name': 'Listing'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'organization_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lineads.Publication']"})
        },
        'lineads.publication': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Publication'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['lineads']
