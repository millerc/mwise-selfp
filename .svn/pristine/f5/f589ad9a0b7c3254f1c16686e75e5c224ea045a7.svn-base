from django.contrib.auth.models import User
from django.db.models import Model, CharField, TextField, FileField, ForeignKey, BooleanField, IntegerField, FloatField, ImageField, DateTimeField, ManyToManyField, SlugField

from core.models import StatusType
from crm.models import Party
from profiles.models import Profile

class Template(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255)
    description = TextField()
    keywords = TextField(null=True,blank=True)
    swatch = ImageField(null=True,blank=True,upload_to="marketwise/templates/swatch",help_text="Small image that shows template color scheme.")
    preview = ImageField(upload_to="marketwise/templates/preview",help_text="Clean version of preview.")
    annotated_preview = ImageField(upload_to="marketwise/templates/annotated",help_text="Version of preview with customization areas marked.")
    rank = FloatField(default=0,help_text="A value used for sorting. Negative or fraction OK.")
    credits_required = IntegerField(help_text="Set to '0' for free templates.")
    color_variations = ManyToManyField('self',null=True,blank=True,related_name='color_variations')
    related_templates = ManyToManyField('self',null=True,blank=True,related_name='related_templates')
    suggested_templates = ManyToManyField('self',null=True,blank=True,related_name='suggested_templates')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/marketwise/template/%s/" % self.slug

    class Meta:
        ordering = ['-rank']

	
class TemplateType(Model):
    description = CharField(max_length=255)
    slug = SlugField(max_length=255,help_text="A URL safe version of the description (prepopulated).")
    parent_type = ForeignKey('self',null=True,blank=True,related_name='children')

    def __unicode__(self):
        return self.description
    
    class Meta:
        ordering = ['parent_type__description', 'description']
        
class TemplateTypeIndustry(TemplateType):
    pass
    
    class Meta:
        verbose_name = "Industry"
        verbose_name_plural = "Industries"

class TemplateTypePurpose(TemplateType):
    industries = ManyToManyField(TemplateTypeIndustry, help_text="Select industries to which this purpose applies.")

    class Meta:
        verbose_name = "Purpose"
        
    def get_absolute_url(self):
        return "/marketwise/interest/%s/" % self.slug


class TemplateTypeFormat(TemplateType):
    pass

    class Meta:
        verbose_name = "Format"
        
class TemplateTypeColor(TemplateType):
    pass
    
    class Meta:
        verbose_name = "Color"

class TemplateClassification(Model):
    template = ForeignKey(Template)
    #template_type = ForeignKey(TemplateType)

class TemplateClassificationIndustry(TemplateClassification):
    industry = ForeignKey(TemplateTypeIndustry)

    class Meta:
        verbose_name = "Industry Classification"
    
class TemplateClassificationPurpose(TemplateClassification):
    purpose = ForeignKey(TemplateTypePurpose)

    class Meta:
        verbose_name = "Purpose Classification"
    
class TemplateClassificationFormat(TemplateClassification):
    format = ForeignKey(TemplateTypeFormat)
    
    class Meta:
        verbose_name = "Format Classification"

class TemplateClassificationColor(TemplateClassification):
    color = ForeignKey(TemplateTypeColor)
    
    class Meta:
        verbose_name = "Color Classification"
        
#class BlockType(Model):
#    name = CharField(max_length=255)
#    
#    def __unicode__(self):
#        return self.NameError

    
class TemplateBlock(Model):
    template = ForeignKey(Template)
    #block_type = ForeignKey(BlockType)
    required = BooleanField(help_text="Sets whether block will be required on customization request form.")
    sequence = IntegerField(help_text="Identifies block with number corresponding to annotated preview. Also used to sort blocks on entry forms.")
    label = CharField(max_length=255,help_text="Short text used to identify block.")
    help_text = CharField(max_length=255,blank=True,null=True,help_text="Additional instructions pertaining to this block.")
    profile_field = CharField(max_length=50, choices=[(field, field) for field in Profile._meta.get_all_field_names()], blank=True, null=True,help_text="Optional user profile field that will be used as default for this block.")

    def __unicode__(self):
        return self.label
        
    class Meta:
        ordering = ['sequence']

class TemplateCharBlock(TemplateBlock):
    default_content = CharField(max_length=255)
    max_length = IntegerField()

class TemplateTextBlock(TemplateBlock):
    default_content = TextField()
    
class TemplateImageBlock(TemplateBlock):
    default_content = ImageField(upload_to='marketwise/templateimageblocks/default_content',blank=True,null=True)

class CustomizationStatusType(StatusType):
    pass
    
class Customization(Model):
    template = ForeignKey(Template)
    #party = ForeignKey(Party)
    user = ForeignKey(User)
    #date_added = DateTimeField()
    status = ForeignKey(CustomizationStatusType,null=True,blank=True)
    deliverable = FileField(null=True,blank=True,upload_to='marketwise/customizations/deliverable')
    added = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return "/marketwise/template/%s/customize/%s/" % (self.template.slug, self.id)
        
    def __unicode__(self):
        return "%s: %s" % (self.user, self.template)
        
    class Meta:
        ordering = ['-updated']


class Block(Model):
    customization = ForeignKey(Customization)
    template_block = ForeignKey(TemplateBlock)

    def __unicode__(self):
        return self.template_block.label

class ImageBlock(Block):
    content = ImageField(upload_to='marketwise/imageblocks/content')
    
class CharBlock(Block):
    content = CharField(max_length=255)    

class TextBlock(Block):
    content = TextField()