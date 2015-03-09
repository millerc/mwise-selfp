from django.db.models import Model, CharField, SlugField

class DaysOfWeek(Model):
    name = CharField(max_length=9)
    
    def __unicode__(self):
        return self.name

class RoleType(Model):
    description = CharField(max_length=255)
    slug = SlugField(max_length=255,help_text="A URL safe version of the description (prepopulated).")

    def __unicode__(self):
        return self.description

class StatusType(Model):
    description = CharField(max_length=255)
    slug = SlugField(max_length=255,help_text="A URL safe version of the description (prepopulated).")
    
    def __unicode__(self):
        return self.description
