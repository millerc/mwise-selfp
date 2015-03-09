# -*- coding: utf-8 -*-

import os 
from uuid import uuid4
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum, Q, Model, CharField, TextField, SlugField, FileField, ForeignKey, BooleanField, IntegerField, FloatField, ImageField, DateTimeField, ManyToManyField, SlugField, PositiveIntegerField, PositiveSmallIntegerField, OneToOneField, EmailField

from core.models import StatusType

def generate_random_uuid():
    return str(uuid4())

def get_design_preview_path(instance, filename):
    return os.path.join('selfpublish', 'templates', str(instance.theme.id), 'preview', filename)
    
def get_design_annotated_path(instance, filename):
    return os.path.join('selfpublish', 'templates', str(instance.theme.id), 'annotated', filename)
    
def get_image_path(instance, filename):
    if instance.user:
        return os.path.join('selfpublish', 'images', str(instance.user.username), filename)
    else:
        return os.path.join('selfpublish', 'images', '_stock', filename)

def get_file_path(instance, filename):
    if instance.user:
        return os.path.join('selfpublish', 'files', str(instance.user.username), filename)
    else:
        return os.path.join('selfpublish', 'files', '_public', filename)

def get_publication_deliverable_path(instance, filename):
    return os.path.join('selfpublish', 'publications', str(instance.id), 'deliverable', filename)

def get_layout_preview_path(instance, filename):
    return os.path.join('selfpublish', 'publications', str(instance.id), 'layouts', filename)

def get_display_ad_path(instance, filename):
    return os.path.join('selfpublish', 'publications', str(instance.ad_ptr.publication.id), 'ads', filename)

def get_listing_logo_path(instance, filename):
    return os.path.join('selfpublish', 'publications', str(instance.ad_ptr.publication.id), 'listings', filename)

class AdSize(Model):
    name = CharField(max_length=32)
    code = CharField(max_length=12)
    width = PositiveSmallIntegerField()
    height = PositiveSmallIntegerField()
    
    def __unicode__(self):
        return "%s (%s)" % (self.name, self.code)
    
    class Meta:
        ordering = ['name']
    
class LineAdCategory(Model):
    name = CharField(max_length=35)
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ['name']
        verbose_name_plural = "line ad categories"

class ImageCategory(Model):
    name = CharField(max_length=80)
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ['name']
        verbose_name_plural = "image categories"
        
class Image(Model):
    user = ForeignKey(User,blank=True,null=True)
    content = ImageField(upload_to=get_image_path)
    credit = CharField(blank=True,null=True,max_length=255)
    caption = TextField(blank=True,null=True)
    categories = ManyToManyField(ImageCategory,blank=True,null=True)

    def filename(self):
        return os.path.basename(self.content.name)
        
    def __unicode__(self):
        return self.filename()
        
class File(Model):
    user = ForeignKey(User,blank=True,null=True)
    content = FileField(upload_to=get_file_path)
    byline = CharField(blank=True,null=True,max_length=255)
    
    def filename(self):
        return os.path.basename(self.content.name)
        
    def __unicode__(self):
        return self.filename()

class PageCount(Model):
    page_count = PositiveSmallIntegerField()
    minimum_articles = PositiveSmallIntegerField()
    maximum_articles = PositiveSmallIntegerField()
    advertisements = PositiveSmallIntegerField()
    listings = PositiveSmallIntegerField()
    revenue = PositiveIntegerField()
    minimum_membership = PositiveSmallIntegerField()
    maximum_membership = PositiveSmallIntegerField()
    setup_fee = PositiveSmallIntegerField()
    encrypted_key = CharField(max_length=44)
    decrypted_key = CharField(max_length=13)
    
    def __unicode__(self):
        return str(self.page_count)

    class Meta:
        ordering = ['page_count']

class SpreadType(Model):
    name = CharField(max_length=20)

    def __unicode__(self):
        return self.name

class SpreadTypeMap(Model):
    page_count = ForeignKey(PageCount)
    sequence = PositiveSmallIntegerField()
    spread_type = ForeignKey(SpreadType)
    default_template = ForeignKey('SpreadTemplate')
    
    def verso(self):
        return self.sequence * 2
    
    def recto(self):
        return self.sequence * 2 + 1
        
    def __unicode__(self):
        if self.sequence == self.page_count.page_count / 2:
            return "%s | %s" % (self.page_count, self.page_count)
        else:
            return "%s | %s-%s" % (self.page_count, self.verso(), self.recto())
        
    class Meta:
       ordering = ['page_count','sequence']
    
class Theme(Model):
    name = CharField(max_length=255,help_text="Descriptive, human friendly name for theme. Can simply be 'Theme 1, Variation 1' or something prettier like 'Autumn Breeze.'")
    slug = SlugField(max_length=15,help_text="Unique, short label for theme and variation corresponding to OTB naming conventions. Examples: THM_001 or THM_001_VAR_001")
    description = TextField(null=True,blank=True)
    keywords = TextField(null=True,blank=True)
    rank = FloatField(default=0,help_text="A value used for sorting. Negative or fraction OK.")
    swatch = ImageField(null=True,blank=True,upload_to="selfpublish/swatches")

    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ['name']

    @models.permalink    
    def get_absolute_url(self):
        return ('selfpublish.views.theme_detail', [str(self.id)])


class Template(Model):
    name = CharField(max_length=255,help_text="Descriptive name for this layout. 'Spread 1' or something more descriptive like 'Feature article with horizontal photo and supporting sidebar article.'")
    slug = SlugField(max_length=7,help_text="Unique, short label for template corresponding to OTB naming conventions. Examples: CVR_001 or SP_001")
    blocks_text = TextField(default="No Blocks")
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class CoverTemplate(Template):
    pass
        
class SpreadTemplate(Template):
    type = ForeignKey(SpreadType)

class Design(Model):
    preview = ImageField(upload_to=get_design_preview_path)
    annotated = ImageField(upload_to=get_design_annotated_path)
    
class CoverDesign(Design):
    theme = OneToOneField(Theme)
    template = ForeignKey(CoverTemplate)

    def __unicode__(self):
        return "%s, %s" % (self.theme, self.template)

class SpreadDesign(Design):
    theme = ForeignKey(Theme)
    template = ForeignKey(SpreadTemplate)

    def __unicode__(self):
        return "%s, %s" % (self.theme, self.template)

class BlockType(Model):
    label = CharField(max_length=255,help_text="Short text used to identify block type")
    
    def __unicode__(self):
        return self.label

    class Meta:
        ordering = ['label']

class TemplateBlock(Model):
    template = ForeignKey(Template)
    type = ForeignKey(BlockType)
    sequence = IntegerField(help_text="Identifies block with number corresponding to annotated preview. Also used to sort blocks on entry forms.")
    help_text = CharField(max_length=255,blank=True,null=True,help_text="Additional instructions pertaining to this block.")

    def save(self, *args, **kwargs):
        super(TemplateBlock, self).save(*args, **kwargs) # Call the "real" save() method.
        self.template.blocks_text = ""
        for tb in self.template.templateblock_set.all():
            self.template.blocks_text = self.template.blocks_text + tb.type.__unicode__() + "\n"
        self.template.save()
            
    def __unicode__(self):
        return "[%s] %s" % (self.sequence, self.type)
        
    class Meta:
        ordering = ['template', 'sequence']

class TemplateCharBlock(TemplateBlock):
    max_length = IntegerField()

class TemplateFileBlock(TemplateBlock):
    target_word_count = PositiveSmallIntegerField(default=500)
    
class TemplateImageBlock(TemplateBlock):
    target_width = PositiveSmallIntegerField(help_text="Target image width in pixels. 32767 maximum.")
    target_height = PositiveSmallIntegerField(help_text="Target image height in pixels. 32767 maximum.")
    
class TemplateAdBlock(TemplateBlock):
    ad_size = ForeignKey(AdSize)
    
class PublicationStatusType(StatusType):
    pass

class Publication(Model):
    title = CharField(max_length=255)
    theme = ForeignKey(Theme)
    page_count = ForeignKey(PageCount)
    owner = ForeignKey(User)
    status = ForeignKey(PublicationStatusType,null=True,blank=True)
    deliverable = FileField(null=True,blank=True,upload_to=get_publication_deliverable_path,help_text="Completed PDF file of publication.")
    added = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)
    progress_bar = PositiveSmallIntegerField(default=1)
    setup_key = CharField(max_length=36,default=generate_random_uuid)
    setup_done = BooleanField()
    listing_price = PositiveSmallIntegerField(default=299)
    
    def blocks_filled_percent(self):
        return int(float(Block.objects.filter(Q(filled=True,layout__spread__publication=self,adblock__isnull=True)|Q(filled=True,layout__cover__publication=self,adblock__isnull=True)).count()) / float(Block.objects.filter(Q(layout__spread__publication=self,adblock__isnull=True)|Q(layout__cover__publication=self,adblock__isnull=True)).count()) * 100)
        
    def lineads_paid(self):
        return self.ad_set.filter(paid=True,displayad__isnull=True).count() * self.listing_price
        
    def displayads_paid(self):
        return self.ad_set.filter(paid=True,linead__isnull=True).aggregate(Sum('displayad__adblock__price'))['displayad__adblock__price__sum']

    def sales_paid(self):
        return self.lineads_paid() + self.displayads_paid()
        
    def lineads_reserved(self):
        return self.ad_set.filter(displayad__isnull=True).count() * self.listing_price
        
    def displayads_reserved(self):
        return self.ad_set.filter(linead__isnull=True).aggregate(Sum('displayad__adblock__price'))['displayad__adblock__price__sum']
        
    def sales_reserved(self):
        return self.lineads_reserved() + self.displayads_reserved()
        
    def get_absolute_url(self):
        return "/self-publish/publication/%s/" % (self.id)
        
    def __unicode__(self):
        return self.title
        
    class Meta:
        ordering = ['-updated']

class LeadStatusType(StatusType):
    pass
    
class Lead(Model):
    publication = ForeignKey(Publication)
    organization = CharField(max_length=128)
    contact_name = CharField(max_length=64)
    phone = CharField(max_length=32,blank=True,null=True)
    email = EmailField(blank=True,null=True)
    note = TextField(blank=True,null=True)
    user = ForeignKey(User,blank=True,null=True)
    status = ForeignKey(LeadStatusType,blank=True,null=True, on_delete=models.SET_NULL)
    invitation_code = CharField(max_length=36,default=generate_random_uuid)
    
    def amount_due(self):
        return self.ad_set.filter(displayad__isnull=True).exclude(paid=True).count() * self.publication.listing_price + (self.ad_set.filter(linead__isnull=True).exclude(paid=True).aggregate(Sum('displayad__adblock__price'))['displayad__adblock__price__sum'] or 0)
    
    def __unicode__(self):
        return self.organization
    
    def get_absolute_url(self):
        return "/self-publish/publication/%s/sales/lead/%s/" % (self.publication.id, self.id)
        
    class Meta:
        ordering = ['organization']
                
class AdPriceLevel(Model):
    name = CharField(max_length=32)
    code = CharField(max_length=16)
    price = PositiveSmallIntegerField()
    ad_size = ForeignKey(AdSize)
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ['name']
    
class Ad(Model):
    publication = ForeignKey(Publication)
    lead = ForeignKey(Lead,blank=True,null=True)
    user = ForeignKey(User,blank=True,null=True)
    setup_key = CharField(max_length=36,default=generate_random_uuid)
    setup_done = BooleanField()
    paid = BooleanField()
    approved = BooleanField()
    
    def __unicode__(self):
        if hasattr(self, 'displayad'):
            return self.displayad.__unicode__()
        else:
            return self.linead.__unicode__()

class DisplayAd(Ad):
    content = FileField(upload_to=get_display_ad_path,blank=True,null=True)
    
    def __unicode__(self):
        return self.adblock.ad_price_level.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('selfpublish.views.displayad_detail', (), {
            'publication_id': self.publication.id,
            'displayad_id': self.pk
            })
    
class LineAd(Ad):
    logo = ImageField(upload_to=get_listing_logo_path,blank=True,null=True)
    category = ForeignKey(LineAdCategory,blank=True,null=True)

    def __unicode__(self):
        if self.adline_set.all():
            return self.adline_set.all()[0].text
        else:
            return "New Listing (%s)" %  self.lead
            
    @models.permalink
    def get_absolute_url(self):
        return('selfpublish.views.linead_detail', (), {
            'publication_id': self.publication.id,
            'linead_id': self.pk
            })
    
    
        #return "/self-publish/sponsor/%s/business-listing/%s/" % (self.publication.id, self.id)
            
class AdLine(Model):
    line_ad = ForeignKey(LineAd)
    sequence = PositiveSmallIntegerField()
    text = CharField(max_length=50)
    
    class Meta:
        ordering = ['sequence']

class Layout(Model):
    progress_bar = PositiveSmallIntegerField(default=1)
    preview = ImageField(blank=True,null=True,upload_to=get_layout_preview_path)

    def get_publication(self):
        try:
            self.spread
        except:
            return self.cover.publication
        else:
            return self.spread.publication
            
    def blocks_filled_count(self):
        return self.block_set.filter(adblock__isnull=True,filled=True).count()
        
    def blocks_filled_percent(self):
        if self.block_set.filter(adblock__isnull=True) and self.block_set.filter(adblock__isnull=True,filled=True).count():
            return int(float(self.blocks_filled_count()) / float(self.block_set.filter(adblock__isnull=True).count()) * 100)
            
    def get_absolute_url(self):
        try:
            self.spread
        except:
            return "/self-publish/publication/%s/layout/%s/" % (self.cover.publication.id, self.id)
        else:
            return "/self-publish/publication/%s/layout/%s/" % (self.spread.publication.id, self.id)

    def __unicode__(self):
        try:
            self.spread
        except:
            return "%s [Cover]" % (self.cover.publication)
        else:
            if self.spread.sequence == self.get_publication().page_count.page_count / 2:
                return "%s [%s]" % (self.spread.publication, self.spread.verso())
            else:
                return "%s [%s-%s]" % (self.spread.publication, self.spread.verso(), self.spread.recto())
    
class Cover(Layout):
    publication = OneToOneField(Publication)
    cover_template = ForeignKey(CoverTemplate)
        
class Spread(Layout):
    publication = ForeignKey(Publication)
    spread_template = ForeignKey(SpreadTemplate)
    sequence = PositiveSmallIntegerField()
    
    def verso(self):
        return self.sequence * 2

    def recto(self):
        if self.sequence < self.publication.page_count.page_count / 2:
            return self.sequence * 2 + 1
        else:
            pass
    
    def design(self):
        return SpreadDesign.objects.get(theme=self.publication.theme,template=self.spread_template)
        
    class Meta:
        ordering = ['sequence']

from selfpublish.forms import BlockForm

class Block(Model):
    layout = ForeignKey(Layout)
    template_block = ForeignKey(TemplateBlock,blank=True,null=True) #
    filled = BooleanField()
    
    def edit_form(self):
        return  BlockForm(self, prefix=str(self.id))   
    
    def __unicode__(self):
        if self.template_block:
            return self.template_block.type.label
        else:
            return "Undefined block"
         
    class Meta:
        ordering = ['template_block__sequence']

    def get_absolute_url(self):
        return "/self-publish/publication/%s/layout/%s/block/%s/" % (self.layout.get_publication().id, self.layout.id, self.id)

class CharBlock(Block):
    template_char_block = ForeignKey(TemplateCharBlock)
    content = CharField(max_length=255,blank=True,null=True)    

    def __unicode__(self):
        return self.template_char_block.type.label

    def save(self, *args, **kwargs):
        super(CharBlock, self).save(*args, **kwargs) # Call the "real" save() method.
        self.block_ptr.template_block = self.template_char_block.templateblock_ptr # Sync parent block template; save joins later
        # Set parent block 'filled' attribute for progress tracking
        if self.content:
            self.block_ptr.filled = True
        else:
            self.block_ptr.filled = False
        self.block_ptr.save()
        self.block_ptr.layout.progress_bar = max([self.block_ptr.layout.blocks_filled_percent(),1]) # Update layout progress bar
        self.block_ptr.layout.save()
        self.block_ptr.layout.get_publication().progress_bar = max([self.block_ptr.layout.get_publication().blocks_filled_percent(),1]) #Update publication progress bar
        self.block_ptr.layout.get_publication().save()

class ImageBlock(Block):
    template_image_block = ForeignKey(TemplateImageBlock)
    image = ForeignKey(Image,blank=True,null=True)
    caption = TextField(blank=True,null=True)

    def get_absolute_url(self):
        return "/self-publish/select-image/%s/" % self.id
        
    def __unicode__(self):
        return self.template_image_block.type.label

    def save(self, *args, **kwargs):
        super(ImageBlock, self).save(*args, **kwargs) # Call the "real" save() method.
        self.block_ptr.template_block = self.template_image_block.templateblock_ptr # Sync parent block template; save joins later
        # Set parent block 'filled' attribute for progress tracking
        if self.image:
            self.block_ptr.filled = True
        else:
            self.block_ptr.filled = False
        self.block_ptr.save()
        self.block_ptr.layout.progress_bar = max([self.block_ptr.layout.blocks_filled_percent(),1]) # Update layout progress bar
        self.block_ptr.layout.save()
        self.block_ptr.layout.get_publication().progress_bar = max([self.block_ptr.layout.get_publication().blocks_filled_percent(),1]) #Update publication progress bar
        self.block_ptr.layout.get_publication().save()

class FileBlock(Block):
    template_file_block = ForeignKey(TemplateFileBlock)
    file = ForeignKey(File,blank=True,null=True)
    
    def __unicode__(self):
        return self.template_file_block.type.label
    
    def save(self, *args, **kwargs):
        super(FileBlock, self).save(*args, **kwargs) # Call the "real" save() method.
        self.block_ptr.template_block = self.template_file_block.templateblock_ptr # Sync parent block template; save joins later
        # Set parent block 'filled' attribute for progress tracking
        if self.file:
            self.block_ptr.filled = True
        else:
            self.block_ptr.filled = False
        self.block_ptr.save()
        self.block_ptr.layout.progress_bar = max([self.block_ptr.layout.blocks_filled_percent(),1]) # Update layout progress bar
        self.block_ptr.layout.save()
        self.block_ptr.layout.get_publication().progress_bar = max([self.block_ptr.layout.get_publication().blocks_filled_percent(),1]) #Update publication progress bar
        self.block_ptr.layout.get_publication().save()
        
class AdBlock(Block):
    template_ad_block = ForeignKey(TemplateAdBlock)
    ad_price_level = ForeignKey(AdPriceLevel)
    display_ad = OneToOneField(DisplayAd,blank=True,null=True, on_delete=models.SET_NULL)
    price = PositiveIntegerField()

    def get_default_price():
        return self.ad_price_level.price
        
    @models.permalink
    def get_absolute_url(self):
        return ('selfpublish.views.reserve_display', (), {
            'publication_id': self.layout.get_publication().id,
            'adblock_id': self.pk
            })

#    def get_absolute_url(self):
#        return "/self-publish/sponsor/%s/premium/%s/" % (self.layout.get_publication().id, self.pk)
    
    def __unicode__(self):
        return self.ad_price_level.name
        
    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.ad_price_level.price
        super(AdBlock,self).save(*args, **kwargs)
        self.block_ptr.template_block = self.template_ad_block.templateblock_ptr
        if self.display_ad:
            if self.display_ad.content:
                self.block_ptr.filled = True
            else:
                self.block_ptr.filled = False
        self.block_ptr.save()
        
