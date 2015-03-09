from django.db import models
from django.contrib.gis.db import models
import rangevaluesfilterspec
import datetime

# Create your models here.

class State(models.Model):
    region = models.CharField(max_length=2)
    division = models.CharField(max_length=2)
    statefp = models.CharField(max_length=2)
    statens = models.CharField(max_length=8)
    stusps = models.CharField(max_length=2)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    lsad = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    funcstat = models.CharField(max_length=1)
    aland = models.FloatField()
    awater = models.FloatField()
    intptlat = models.CharField(max_length=11)
    intptlon = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

class County(models.Model):
    state = models.ForeignKey('State', null=True, blank=True)
    statefp = models.CharField(max_length=2)
    countyfp = models.CharField(max_length=3)
    countyns = models.CharField(max_length=8)
    cntyidfp = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    namelsad = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    classfp = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    csafp = models.CharField(max_length=3)
    cbsafp = models.CharField(max_length=5)
    metdivfp = models.CharField(max_length=5)
    funcstat = models.CharField(max_length=1)
    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Counties"

    def __unicode__(self):
        return u'%s, %s' % (self.namelsad, self.state)


class Place(models.Model):
    state = models.ForeignKey('State', null=True, blank=True)
    counties = models.ManyToManyField('County', null=True, blank=True)
    zip_codes = models.ManyToManyField('ZipCode', null=True, blank=True)
    primary_zip_code = models.CharField(max_length=5, null=True, blank=True)
    current_population = models.PositiveIntegerField(null=True, blank=True)
    current_population.list_filter_range = [1000, 5000, 10000, 15000, 20000, 25000, 35000, 50000, 75000, 100000, 200000, 500000]
    elevation = models.IntegerField(null=True, blank=True)
    geonameid = models.IntegerField(null=True, blank=True)
    twitter_query = models.CharField(max_length=140, null=True, blank=True)
    statefp = models.CharField(max_length=2)
    placefp = models.CharField(max_length=5)
    placens = models.CharField(max_length=8)
    plcidfp = models.CharField(max_length=7)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    namelsad = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    classfp = models.CharField(max_length=2)
    cpi = models.CharField(max_length=1)
    pcicbsa = models.CharField(max_length=1)
    pcinecta = models.CharField(max_length=1)
    mtfcc = models.CharField(max_length=5)
    funcstat = models.CharField(max_length=1)
    point = models.PointField(srid=4269, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return u'%s, %s' % (self.name, self.state)
        
    def county_list(self):
        return ', '.join([a_county.name for a_county in self.counties.all()])

    def get_links(self):
        return self.link_set.filter(published=True)

    def get_categorizations(self):
        return Categorization.objects.filter(link__place=self,link__published=True)
    
class ZipCode(models.Model):
    zcta5ce = models.CharField(max_length=5)
    classfp = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    funcstat = models.CharField(max_length=1)
    aland = models.FloatField()
    awater = models.FloatField()
    intptlat = models.CharField(max_length=11)
    intptlon = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()
    
    class Meta:
        ordering = ('zcta5ce',)

    def __unicode__(self):
        return self.zcta5ce

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.name
    
class Link(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(verify_exists=True)
    place = models.ManyToManyField('Place', through='Listing')
    categories = models.ManyToManyField('Category', through='Categorization')
    description = models.TextField(null=True,blank=True,help_text='Only the first 60 words will be displayed. No URLs allowed in description.')
    featured = models.BooleanField()
    published = models.BooleanField()
    objects = models.GeoManager()

    def get_places(self):
        return self.place_set.all()

    def category_list(self):
        return '; '.join([category.name for category in self.categories.all()])

    def place_list(self):
        return '; '.join([a_place.name + ', ' + a_place.state.name for a_place in self.place.all()])

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('-featured','name',)


class Listing(models.Model):
    link = models.ForeignKey('Link')
    place = models.ForeignKey('Place')
    date_added = models.DateField()
    objects = models.GeoManager()

    def was_added_today(self):
        return self.date_added >= datetime.date.today()

    class Meta:
       get_latest_by = 'date_added'
       ordering = ('-date_added',)

    def __unicode__(self): return '%s in %s' % (self.link, self.place)
    
class Categorization(models.Model):
    link = models.ForeignKey('Link')
    category = models.ForeignKey('Category')
    class Meta:
        ordering = ('category','link',)
    def __unicode__(self): return '%s in %s' % (self.link, self.category)


