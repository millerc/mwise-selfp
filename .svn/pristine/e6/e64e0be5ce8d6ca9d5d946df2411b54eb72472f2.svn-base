import os

from django.db import models

from core import DaysOfWeek

def get_video_path(instance, filename):
    return os.path.join('barzconnect', 'video', str(instance.venue.id), filename)

def get_photo_path(instance, filename):
    return os.path.join('barzconnect', 'photo', str(instance.venue.id), str(instance.poi.id), filename)


# Create your models here.


class Category(Model):
    name = CharField(max_length=35)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"


class Venue(Model):
    name = CharField(max_length=45)
    categories = ManyToManyField(Category)
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ('name',)


class Tour(Model):
    name = CharField(max_length=45)
    venue = ForeignKey(Venue)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class BarZBase(Model):
    name = CharField(max_length=45)
    description = TextField(blank=True,null=True)
    phone = CharField(max_length=12,blank=True,null=True)
    url = models.URLField(verify_exists=False,null=True,blank=True)    
    email = EmailField(blank=True,null=True)
    video = FileField(null=True,blank=True,upload_to=get_video_path)
    facebook = models.URLField(verify_exists=False,null=True,blank=True)
    twitter = models.URLField(verify_exists=False,null=True,blank=True)


class POI(Model):
    venue = ForeignKey(Venue)
    tour = ForeignKey(Tour,blank=True,null=True)
    description_word_limit = PositiveIntegerField(default=0)
    address = CharField(max_length=255,blank=True,null=True)
    video = FileField(null=True,blank=True,upload_to=get_video_path)
    category_limit = PositiveIntegerField(default=0)
    categories = ManyToManyField(Category,blank=True,null=True)
    facebook_enable = models.BooleanField()
    twitter_enable = models.BooleanField()
    point = models.PointField(srid=4326,null=True,blank=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

class Photo(model):
    image = ImageField(upload_to=get_photo_path,blank=True,null=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    
    def __unicode__(self):
        return self.name
        
    
class Deal(model):
    name = models.CharField(max_length=45)
    tour = models.ForeighKey(Tour,blank=True,null=True)
    poi = models.ForeignKey(POI,blank=True,null=True)
    description = TextField(blank=True,null=True)
    photo =?
    start = models.DateTimeField()
    end = models.DateTimeField()
    REPEAT_CHOICES = (
        ('N', 'Does not'),
        ('W', 'Weekly'),
        ('M', 'Monthly')
    )
    repeat = models.CharField(max_length=1, choices=REPEAT_CHOICES)
    repeat_days = models.ManyToManyField(DaysOfWeek,blank=True,null=True)
    repeat_end = models.DateTimeField(blank=True,null=True)
    phone = CharField(max_length=12,blank=True,null=True)
    url = models.URLField(verify_exists=False,null=True,blank=True)
    email = EmailField(blank=True,null=True)
    facebook = models.URLField(verify_exists=False,null=True,blank=True)
    twitter = models.URLField(verify_exists=False,null=True,blank=True)
 
    def __unicode__(self):
        return self.name
   
class Event(model):
    name = models.CharField(max_length=45)
    description = TextField(blank=True,null=True)
    address = CharField(max_length=255,blank=True,null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    REPEAT_CHOICES = (
        ('N', 'Does not'),
        ('W', 'Weekly'),
        ('M', 'Monthly')
    )
    repeat = models.CharField(max_length=1, choices=REPEAT_CHOICES)
    repeat_days = models.ManyToManyField(DaysOfWeek,blank=True,null=True)
    repeat_end = models.DateTimeField(blank=True,null=True)
    photo = ?
    url = models.URLField(verify_exists=False,null=True,blank=True)
    email = EmailField(blank=True,null=True)
    *cost = CharField(blank=True,null=True,max_length=40)
    video = FileField(null=True,blank=True,upload_to=get_video_path)
    facebook = models.URLField(verify_exists=False,null=True,blank=True)
    twitter = models.URLField(verify_exists=False,null=True,blank=True)
 
    def __unicode__(self):
        return self.name
    

    