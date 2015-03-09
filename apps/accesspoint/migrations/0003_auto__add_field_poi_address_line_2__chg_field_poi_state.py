# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'POI.address_line_2'
        db.add_column('accesspoint_poi', 'address_line_2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Renaming column for 'POI.state' to match new field type.
        db.rename_column('accesspoint_poi', 'state_id', 'state')
        # Changing field 'POI.state'
        db.alter_column('accesspoint_poi', 'state', self.gf('django.db.models.fields.CharField')(max_length=63, null=True))

        # Removing index on 'POI', fields ['state']
        db.delete_index('accesspoint_poi', ['state_id'])


    def backwards(self, orm):
        
        # Adding index on 'POI', fields ['state']
        db.create_index('accesspoint_poi', ['state_id'])

        # Deleting field 'POI.address_line_2'
        db.delete_column('accesspoint_poi', 'address_line_2')

        # Renaming column for 'POI.state' to match new field type.
        db.rename_column('accesspoint_poi', 'state', 'state_id')
        # Changing field 'POI.state'
        db.alter_column('accesspoint_poi', 'state_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hub.State'], null=True))


    models = {
        'accesspoint.category': {
            'Meta': {'ordering': "('description',)", 'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'accesspoint.chamber': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Chamber', '_ormbases': ['accesspoint.POI']},
            'places': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['hub.Place']", 'null': 'True', 'blank': 'True'}),
            'poi_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['accesspoint.POI']", 'unique': 'True', 'primary_key': 'True'})
        },
        'accesspoint.communitylist': {
            'Meta': {'object_name': 'CommunityList'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'places': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['hub.Place']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'accesspoint.event': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Event', '_ormbases': ['accesspoint.POI']},
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'poi_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['accesspoint.POI']", 'unique': 'True', 'primary_key': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {})
        },
        'accesspoint.member': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Member', '_ormbases': ['accesspoint.POI']},
            'chamber': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accesspoint.Chamber']", 'null': 'True', 'blank': 'True'}),
            'poi_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['accesspoint.POI']", 'unique': 'True', 'primary_key': 'True'})
        },
        'accesspoint.poi': {
            'Meta': {'ordering': "('name',)", 'object_name': 'POI'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['accesspoint.Category']", 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '63', 'null': 'True', 'blank': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '4269', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '63', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'hub.county': {
            'Meta': {'ordering': "('name',)", 'object_name': 'County'},
            'cbsafp': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'classfp': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'cntyidfp': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'countyfp': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'countyns': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'csafp': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'funcstat': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '4269'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lsad': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'metdivfp': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'mtfcc': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'namelsad': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'db_index': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hub.State']", 'null': 'True', 'blank': 'True'}),
            'statefp': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'hub.place': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Place'},
            'classfp': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'counties': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['hub.County']", 'null': 'True', 'blank': 'True'}),
            'cpi': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'current_population': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'elevation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'funcstat': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '4269'}),
            'geonameid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lsad': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'mtfcc': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'namelsad': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pcicbsa': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'pcinecta': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'placefp': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'placens': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'plcidfp': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '4269', 'null': 'True', 'blank': 'True'}),
            'primary_zip_code': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'db_index': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hub.State']", 'null': 'True', 'blank': 'True'}),
            'statefp': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'twitter_query': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'zip_codes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['hub.ZipCode']", 'null': 'True', 'blank': 'True'})
        },
        'hub.state': {
            'Meta': {'ordering': "('name',)", 'object_name': 'State'},
            'aland': ('django.db.models.fields.FloatField', [], {}),
            'awater': ('django.db.models.fields.FloatField', [], {}),
            'division': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'funcstat': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '4269'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intptlat': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'intptlon': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'lsad': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'mtfcc': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'db_index': 'True'}),
            'statefp': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'statens': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'stusps': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'hub.zipcode': {
            'Meta': {'ordering': "('zcta5ce',)", 'object_name': 'ZipCode'},
            'aland': ('django.db.models.fields.FloatField', [], {}),
            'awater': ('django.db.models.fields.FloatField', [], {}),
            'classfp': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'funcstat': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '4269'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intptlat': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'intptlon': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'mtfcc': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'zcta5ce': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['accesspoint']
