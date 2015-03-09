# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('accesspoint_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('accesspoint', ['Category'])

        # Adding model 'POI'
        db.create_table('accesspoint_poi', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hub.State'], null=True, blank=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=4269, null=True, blank=True)),
        ))
        db.send_create_signal('accesspoint', ['POI'])

        # Adding M2M table for field categories on 'POI'
        db.create_table('accesspoint_poi_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('poi', models.ForeignKey(orm['accesspoint.poi'], null=False)),
            ('category', models.ForeignKey(orm['accesspoint.category'], null=False))
        ))
        db.create_unique('accesspoint_poi_categories', ['poi_id', 'category_id'])

        # Adding model 'Chamber'
        db.create_table('accesspoint_chamber', (
            ('poi_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accesspoint.POI'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('accesspoint', ['Chamber'])

        # Adding M2M table for field places on 'Chamber'
        db.create_table('accesspoint_chamber_places', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('chamber', models.ForeignKey(orm['accesspoint.chamber'], null=False)),
            ('place', models.ForeignKey(orm['hub.place'], null=False))
        ))
        db.create_unique('accesspoint_chamber_places', ['chamber_id', 'place_id'])

        # Adding model 'Member'
        db.create_table('accesspoint_member', (
            ('poi_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accesspoint.POI'], unique=True, primary_key=True)),
            ('chamber', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accesspoint.Chamber'], null=True, blank=True)),
        ))
        db.send_create_signal('accesspoint', ['Member'])

        # Adding model 'Event'
        db.create_table('accesspoint_event', (
            ('poi_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accesspoint.POI'], unique=True, primary_key=True)),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('accesspoint', ['Event'])

        # Adding model 'CommunityList'
        db.create_table('accesspoint_communitylist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal('accesspoint', ['CommunityList'])

        # Adding M2M table for field places on 'CommunityList'
        db.create_table('accesspoint_communitylist_places', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('communitylist', models.ForeignKey(orm['accesspoint.communitylist'], null=False)),
            ('place', models.ForeignKey(orm['hub.place'], null=False))
        ))
        db.create_unique('accesspoint_communitylist_places', ['communitylist_id', 'place_id'])


    def backwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('accesspoint_category')

        # Deleting model 'POI'
        db.delete_table('accesspoint_poi')

        # Removing M2M table for field categories on 'POI'
        db.delete_table('accesspoint_poi_categories')

        # Deleting model 'Chamber'
        db.delete_table('accesspoint_chamber')

        # Removing M2M table for field places on 'Chamber'
        db.delete_table('accesspoint_chamber_places')

        # Deleting model 'Member'
        db.delete_table('accesspoint_member')

        # Deleting model 'Event'
        db.delete_table('accesspoint_event')

        # Deleting model 'CommunityList'
        db.delete_table('accesspoint_communitylist')

        # Removing M2M table for field places on 'CommunityList'
        db.delete_table('accesspoint_communitylist_places')


    models = {
        'accesspoint.category': {
            'Meta': {'ordering': "('description',)", 'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'accesspoint.chamber': {
            'Meta': {'object_name': 'Chamber', '_ormbases': ['accesspoint.POI']},
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
            'Meta': {'object_name': 'Event', '_ormbases': ['accesspoint.POI']},
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'poi_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['accesspoint.POI']", 'unique': 'True', 'primary_key': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {})
        },
        'accesspoint.member': {
            'Meta': {'object_name': 'Member', '_ormbases': ['accesspoint.POI']},
            'chamber': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accesspoint.Chamber']", 'null': 'True', 'blank': 'True'}),
            'poi_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['accesspoint.POI']", 'unique': 'True', 'primary_key': 'True'})
        },
        'accesspoint.poi': {
            'Meta': {'object_name': 'POI'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['accesspoint.Category']", 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '4269', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hub.State']", 'null': 'True', 'blank': 'True'}),
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
