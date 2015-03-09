from django.conf.urls.defaults import *
from marketwise.models import Template, TemplateTypePurpose

templates = {
    'queryset': Template.objects.all(),
}
purposes = {
    'queryset': TemplateTypePurpose.objects.all(),
}

urlpatterns = patterns('',
    (r'^free-templates/$', 'marketwise.views.templates', {'free_templates': True}, "free_templates",),
    (r'^templates/search/$', 'marketwise.views.template_search',),
    (r'^templates/$', 'marketwise.views.templates', {'free_templates': ''}, "all_templates",),
    (r'^template/(?P<template_slug>[-\w]+)/customize/(?P<id>[\d]+)/$', 'marketwise.views.customization_detail',),
    (r'^template/(?P<slug>[-\w]+)/customize/$', 'marketwise.views.template_customize',),
    (r'^template/(?P<slug>[-\w]+)/$', 'marketwise.views.template_detail',),
    (r'^interest/(?P<parent_slug>[-\w]+)/(?P<slug>[-\w]+)/$', 'marketwise.views.templates_by_purpose',),
    (r'^interest/(?P<slug>[-\w]+)/$', 'marketwise.views.templates_by_purpose', {'parent_slug': ''}),
    (r'^dashboard/$', 'marketwise.views.dashboard', {}, "marketwise_dashboard"),
    (r'^$', 'marketwise.views.home', {}, "marketwise_home"),

)
