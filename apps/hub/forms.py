from django import forms
from django.forms import ModelForm
from models import *

class URLForm(forms.Form):
    url = forms.URLField(verify_exists=True)

class LinkForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    name = forms.CharField(max_length=100, label='Link title')
    
    class Meta:
        model = Link
        fields = ['name','url','description',]
