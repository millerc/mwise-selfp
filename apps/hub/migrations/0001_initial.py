# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'State'
        db.create_table('hub_state', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('division', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('statefp', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('statens', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('stusps', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100, db_index=True)),
            ('lsad', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('mtfcc', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('funcstat', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('aland', self.gf('django.db.models.fields.FloatField')()),
            ('awater', self.gf('django.db.models.fields.FloatField')()),
            ('intptlat', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('intptlon', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=4269)),
        ))
        db.send_create_signal('hub', ['State'])

        # Adding model 'County'
        db.create_table('hub_county', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hub.State'], null=True, blank=True)),
            ('statefp', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('countyfp', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('countyns', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('cntyidfp', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100, db_index=True)),
            ('namelsad', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('lsad', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('classfp', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('mtfcc', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('csafp', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('cbsafp', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('metdivfp', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('funcstat', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=4269)),
        ))
        db.send_create_signal('hub', ['County'])

        # Adding model 'Place'
        db.create_table('hub_place', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hub.State'], null=True, blank=True)),
            ('primary_zip_code', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('current_population', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('elevation', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('geonameid', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('twitter_query', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
            ('statefp', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('placefp', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('placens', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('plcidfp', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100, db_index=True)),
            ('namelsad', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('lsad', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('classfp', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('cpi', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('pcicbsa', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('pcinecta', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('mtfcc', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('funcstat', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=4269, null=True, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=4269)),
        ))
        db.send_create_signal('hub', ['Place'])

        # Adding M2M table for field counties on 'Place'
        db.create_table('hub_place_counties', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('place', models.ForeignKey(orm['hub.place'], null=False)),
            ('county', models.ForeignKey(orm['hub.county'], null=False))
        ))
        db.create_unique('hub_place_counties', ['place_id', 'county_id'])

        # Adding M2M table for field zip_codes on 'Place'
        db.create_table('hub_place_zip_codes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('place', models.ForeignKey(orm['hub.place'], null=False)),
            ('zipcode', models.ForeignKey(orm['hub.zipcode'], null=False))
        ))
        db.create_unique('hub_place_zip_codes', ['place_id', 'zipcode_id'])

        # Adding model 'ZipCode'
        db.create_table('hub_zipcode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zcta5ce', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('classfp', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('mtfcc', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('funcstat', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('aland', self.gf('django.db.models.fields.FloatField')()),
            ('awater', self.gf('django.db.models.fields.FloatField')()),
            ('intptlat', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('intptlon', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=4269)),
        ))
        db.send_create_signal('hub', ['ZipCode'])

        # Adding model 'Category'
        db.create_table('hub_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('hub', ['Category'])

        # Adding model 'Link'
        db.create_table('hub_link', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('hub', ['Link'])

        # Adding model 'Listing'
        db.create_table('hub_listing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hub.Link'])),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hub.Place'])),
            ('date_added', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('hub', ['Listing'])

        # Adding model 'Categorization'
        db.create_table('hub_categorization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hub.Link'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hub.Category'])),
        ))
        db.send_create_signal('hub', ['Categorization'])


    def backwards(self, orm):
        
        # Deleting model 'State'
        db.delete_table('hub_state')

        # Deleting model 'County'
        db.delete_table('hub_county')

        # Deleting model 'Place'
        db.delete_table('hub_place')

        # Removing M2M table for field counties on 'Place'
        db.delete_table('hub_place_counties')

        # Removing M2M table for field zip_codes on 'Place'
        db.delete_table('hub_place_zip_codes')

        # Deleting model 'ZipCode'
        db.delete_table('hub_zipcode')

        # Deleting model 'Category'
        db.delete_table('hub_category')

        # Deleting model 'Link'
        db.delete_table('hub_link')

        # Deleting model 'Listing'
        db.delete_table('hub_listing')

        # Deleting model 'Categorization'
        db.delete_table('hub_categorization')


    models = {
        'hub.categorization': {
            'Meta': {'ordering': "('category', 'link')", 'object_name': 'Categorization'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hub.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hub.Link']"})
        },
        'hub.category': {
            'Meta': {'ordering': "['name']", 'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'db_index': 'True'})
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
        'hub.link': {
            'Meta': {'ordering': "('-featured', 'name')", 'object_name': 'Link'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['hub.Category']", 'through': "orm['hub.Categorization']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'place': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['hub.Place']", 'through': "orm['hub.Listing']", 'symmetrical': 'False'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'hub.listing': {
            'Meta': {'ordering': "('-date_added',)", 'object_name': 'Listing'},
            'date_added': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hub.Link']"}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hub.Place']"})
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

    complete_apps = ['hub']
