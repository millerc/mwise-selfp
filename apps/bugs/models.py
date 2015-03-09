from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

PROJECT_CHOICES = (
    ('accesspoint', 'AccessPoint'),
    ('barzconnect', 'BarZ Connect'),
    ('cloud', 'Cloud'),
    ('marketwise', 'Marketwise'),
    ('selfpublish', 'Self Publishing'),
	)
	
STATUS_CODES = (
    (1, 'Open'),
    (2, 'Working'),
    (3, 'Closed'),
    )

PRIORITY_CODES = (
    (1, 'Now'),
    (2, 'Soon'),
    (3, 'Someday'),
    )
    
class Ticket(models.Model):
    """Trouble tickets"""
    title = models.CharField(max_length=100)
    project = models.CharField(blank=True, max_length=100, choices=PROJECT_CHOICES)
    submitted_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    submitter = models.ForeignKey(User, related_name="submitter")
    assigned_to = models.ForeignKey(User)
    description = models.TextField(blank=True)
    status = models.IntegerField(default=1, choices=STATUS_CODES)
    priority = models.IntegerField(default=1, choices=PRIORITY_CODES)

    class Meta:
        ordering = ('status', 'priority', 'submitted_date', 'title')

    def __unicode__(self):
        return self.title

class Attachment(models.Model):
    ticket = models.ForeignKey(Ticket)
    attachment = models.FileField(upload_to="bugs/attachments")
    
    def save(self, *args, **kwargs):
        super(Attachment, self).save(*args, **kwargs) # Call the "real" save() method.
        self.ticket.save()
    
class Comment(models.Model):
    ticket = models.ForeignKey(Ticket)
    comment = models.TextField()

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs) # Call the "real" save() method.
        self.ticket.save()
