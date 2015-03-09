from django import forms
from django.utils.datastructures import SortedDict
from django.template.defaultfilters import slugify
from marketwise.models import TemplateTypeColor, TemplateTypeFormat
from marketwise.widgets import CheckboxSelectMultipleAllNone

class TemplateSearchForm(forms.Form):
    q = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'searchfield'}))

class TemplateFilterForm(forms.Form):
    colors = forms.ModelMultipleChoiceField(
        queryset=TemplateTypeColor.objects.all(), 
        required=False, 
        widget=CheckboxSelectMultipleAllNone
        )
    formats = forms.ModelMultipleChoiceField(
        queryset=TemplateTypeFormat.objects.all(), 
        required=False, 
        widget=CheckboxSelectMultipleAllNone
        )
    q = forms.CharField(required=False,widget=forms.widgets.HiddenInput())



class CustomizeTemplateForm(forms.Form):
    def __init__(self, template, request, *args, **kwargs):
        super(CustomizeTemplateForm, self).__init__(*args, **kwargs)
        for b in template.templateblock_set.all():
            try:
                b.templatecharblock
            except:
                pass
            else:
                self.fields[b.label] = forms.CharField(
                    required=b.required,
                    label=b.label,
                    initial=b.templatecharblock.default_content,
                    help_text=b.help_text,
                    max_length=b.templatecharblock.max_length
                    )
                if b.profile_field:
                    self.fields[b.label].initial=getattr(request.user.get_profile(),str(b.profile_field))
                #else:
                    #self.fields[b.label].initial=b.templatecharblock.default_content
            try:
                b.templatetextblock
            except:
                pass
            else:
                self.fields[b.label] = forms.CharField(
                    required=b.required,label=b.label,initial=b.templatetextblock.default_content,help_text=b.help_text,widget=forms.Textarea
                    )
            try:
               b.templateimageblock
            except:
                pass
            else:
                self.fields[b.label] = forms.ImageField(required=b.required,label=b.label,help_text=b.help_text)


def make_custom_form(template):
    fields = SortedDict([])
    blocks = template.templateblock_set.all().order_by('sequence')
    for b in blocks:
        try:
            b.templatecharblock
        except:
            pass
        else:
            fields[b.label] = forms.CharField(
                required=b.required,label=b.label,initial=b.templatecharblock.default_content,help_text=b.help_text,max_length=b.templatecharblock.max_length
                )
        try:
            b.templatetextblock
        except:
            pass
        else:
            fields[b.label] = forms.CharField(
                required=b.required,label=b.label,initial=b.templatetextblock.default_content,help_text=b.help_text,widget=forms.Textarea
                )
        try:
           b.templateimageblock
        except:
            pass
        else:
            fields[b.label] = forms.ImageField(required=b.required,label=b.label,help_text=b.help_text)
                        
    return type('TemplateCustomizationForm', (forms.BaseForm,), { 'base_fields': fields })
    
