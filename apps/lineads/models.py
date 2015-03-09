import os
from django.db import models

# Create your models here.

def get_listing_logo_path(instance, filename):
    return os.path.join('lineads', str(instance.publication.job_code), filename)
    

class Publication(models.Model):
    name = models.CharField(max_length=255)
    job_code = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        
class Listing(models.Model):
    publication = models.ForeignKey(Publication)
    logo = models.ImageField(upload_to=get_listing_logo_path)
    organization_name = models.CharField(max_length=120)
    contact_name = models.CharField(blank=True,null=True,max_length=60)
    address = models.TextField()
    phone = models.CharField(max_length=30)
    description = models.TextField()

    def __unicode__(self):
        return self.organization_name

    class Meta:
        ordering = ('organization_name',)
        
