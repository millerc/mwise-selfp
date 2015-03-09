from django.db import models
from django.contrib.gis.db import models

from django.contrib.auth.models import User
from hub.models import State, Place

class Category(models.Model):
    description = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.description

    class Meta:
        ordering = ('description',)
        verbose_name_plural = "Categories"

class POI(models.Model):
    published = models.BooleanField()
    name = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    address_line_2 = models.CharField(max_length=255,null=True,blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    state = models.CharField(max_length=63,null=True,blank=True)
    zip = models.CharField(max_length=10,null=True,blank=True)
    phone = models.CharField(max_length=63,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    url = models.URLField(verify_exists=False,null=True,blank=True)
    point = models.PointField(srid=4269,null=True,blank=True)
    categories = models.ManyToManyField(Category,null=True,blank=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "POI"

class Chamber(POI):
    places = models.ManyToManyField(Place,null=True,blank=True,help_text='Census places served by this Chamber')

class Member(POI):
    chamber = models.ForeignKey(Chamber,null=True,blank=True)

class Event(POI):
    start = models.DateTimeField()
    end = models.DateTimeField()

class CommunityList(models.Model):
    user = models.OneToOneField(User)
    places = models.ManyToManyField(Place,null=True,blank=True)
    
    
    