# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm

from selfpublish.models import *

class MemberSelectPageChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%i-%i" % (obj.minimum_membership, obj.maximum_membership)

class MembershipSelectForm(forms.Form):
    membership = MemberSelectPageChoiceField(queryset=PageCount.objects.exclude(page_count=8), empty_label="Select Membership Size")

class PublicationSetupForm(forms.Form):
    decrypted_key = forms.CharField(max_length=13, label="Key", help_text="Provided at checkout. Example: OTB12-ABCD345")
    title = forms.CharField(max_length=255, help_text="Please give the new publication a title.")

class BlockForm(forms.Form):
    def __init__(self, block, *args, **kwargs):
        super(BlockForm, self).__init__(*args, **kwargs)
        if hasattr(block, 'charblock'):
            help_text="(%s characters max)" % block.template_block.templatecharblock.max_length
            self.fields[block.template_block.type.label] = forms.CharField(
                required=False,
                label="",
                help_text=help_text,
                initial=block.charblock.content,
                widget=forms.TextInput(attrs={'size':min(60,block.template_block.templatecharblock.max_length)}),
                max_length=block.template_block.templatecharblock.max_length
                )
        if hasattr(block, 'fileblock'):
            if block.fileblock.file:
                initial = {'file': block.fileblock.file.id, 'byline': block.fileblock.file.byline}
            else:
                initial = {'file': None, 'byline': None}
#             self.fields['file'] = forms.ModelChoiceField(
#                 required=False,
#                 label='Choose an existing file',
#                 queryset=File.objects.filter(user=block.layout.get_publication().owner),
#                 initial=initial['file']
#                 )
            self.fields['uploadedfile'] = forms.FileField(
                required=False,
                label='Upload document'
                )
            self.fields['byline'] = forms.CharField(
                required=False,
                label='Byline',
                initial=initial['byline'],
                max_length=255
                )
        if hasattr(block, 'imageblock'):
            if block.imageblock.image:
                initial = {'image': block.imageblock.image.id, 'credit': block.imageblock.image.credit, 'caption': block.imageblock.caption}
            else:
                initial = {'image': None, 'credit': None, 'caption': None}
#             self.fields['image'] = forms.ModelChoiceField(
#                 required=False,
#                 label='Choose an existing image',
#                 queryset=Image.objects.filter(user=block.layout.get_publication().owner),
#                 initial=initial['image']
#                 )
            self.fields['uploadedimage'] = forms.ImageField(
                required=False,
                label='Upload image'
                )
            self.fields['credit'] = forms.CharField(
                required=False,
                label='Credit',
                initial=initial['credit'],
                widget=forms.TextInput(attrs={'size':'40'}),
                max_length=255
                )
            self.fields['caption'] = forms.CharField(
                required=False,
                label='Caption',
                initial=initial['caption'],
                widget=forms.Textarea
                )
                
class BlockConflictForm(forms.Form):
    def __init__(self, block_conflicts, new_design, *args, **kwargs):
        super(BlockConflictForm, self).__init__(*args, **kwargs)
        self.fields['new_design'] = forms.ModelChoiceField(queryset=Design.objects.filter(pk=new_design.pk),initial=new_design.pk,widget=forms.HiddenInput)
        for block in block_conflicts:
            self.fields['b'+str(block.pk)] = forms.ModelChoiceField(
            required=False,
            label='['+str(block.template_block.sequence)+'] '+block.template_block.type.label,
            queryset=TemplateBlock.objects.filter(template=new_design.template,type=block.template_block.type),
            empty_label='Do not use this item'
            )

class ImageFilterForm(forms.Form):
    filter = forms.ModelChoiceField(required=False,label='',queryset=ImageCategory.objects.all(),empty_label='My Images')

class LayoutForm(forms.Form):
    def __init__(self, layout, *args, **kwargs):
        super(LayoutForm, self).__init__(*args, **kwargs)
        for block in layout.block_set.all():
            prefix = str(block.id)+'-'
            if hasattr(block, 'charblock'):
                self.fields[prefix+block.template_block.type.label] = forms.CharField(
                    required=False,
                    label=block.template_block.type.label,
                    initial=block.charblock.content,
                    max_length=block.template_block.templatecharblock.max_length
                    )
            if hasattr(block, 'fileblock'):
                if block.fileblock.file:
                    initial = {'file': block.fileblock.file.id, 'byline': block.fileblock.file.byline}
                else:
                    initial = {'file': None, 'byline': None}
                self.fields[prefix+'file'] = forms.ModelChoiceField(
                    required=False,
                    label='Choose an existing file',
                    queryset=File.objects.filter(user=block.layout.get_publication().owner),
                    initial=initial['file']
                    )
                self.fields[prefix+'uploadedfile'] = forms.FileField(
                    required=False,
                    label='Upload a new file'
                    )
                self.fields[prefix+'byline'] = forms.CharField(
                    required=False,
                    label='Byline',
                    initial=initial['byline'],
                    max_length=255
                    )
            if hasattr(block, 'imageblock'):
                if block.imageblock.image:
                    initial = {'image': block.imageblock.image.id, 'credit': block.imageblock.image.credit, 'caption': block.imageblock.caption}
                else:
                    initial = {'image': None, 'credit': None, 'caption': None}
                self.fields[prefix+'uploadedimage'] = forms.ImageField(
                    required=False,
                    label='Upload a new image'
                    )
                self.fields[prefix+'credit'] = forms.CharField(
                    required=False,
                    label='Credit',
                    initial=initial['credit'],
                    max_length=255
                    )
                self.fields[prefix+'caption'] = forms.CharField(
                    required=False,
                    label='Caption',
                    initial=initial['caption'],
                    widget=forms.Textarea
                    )

class LeadEditForm(forms.ModelForm):
    class Meta:
        model = Lead
        exclude = ('publication','user','status','invitation_code')
        
class LeadImportForm(forms.Form):
    file = forms.FileField(required=True)
    
class LeadImportMapForm(forms.Form):
    def __init__(self, import_fields, *args, **kwargs):
        super(LeadImportMapForm, self).__init__(*args, **kwargs)
        import_field_choices = [('','---------' )] + [(f, f) for f in import_fields]
        self.fields['organization'] = forms.ChoiceField(
            required=True,
            choices=import_field_choices
            )
        self.fields['contact'] = forms.ChoiceField(
            required=True,
            choices=import_field_choices
            )
        self.fields['phone'] = forms.ChoiceField(
            required=False,
            choices=import_field_choices
            )
        self.fields['email'] = forms.ChoiceField(
            required=False,
            choices=import_field_choices
            )
        self.fields['note'] = forms.ChoiceField(
            required=False,
            choices=import_field_choices
            )

class LineAdForm(forms.ModelForm):
    class Meta:
        model = LineAd
        exclude = ('publication','lead','user','setup_key','setup_done','paid',)
        
class DisplayAdForm(forms.ModelForm):
    class Meta:
        model = DisplayAd
        fields = ('content',)
        
class DisplayAdReservationForm(forms.Form):
    def __init__(self, adblocks, *args, **kwargs):
        super(DisplayAdReservationForm, self).__init__(*args, **kwargs)
        self.fields['adspace'] = forms.ModelChoiceField(
            queryset=adblocks
            )
        self.fields['listing'] = forms.BooleanField(required=False)
        
class LeadSearchForm(forms.Form):
    search = forms.CharField(required=False)
    status = forms.ModelChoiceField(queryset=LeadStatusType.objects.all(),required=False,empty_label="All")
    