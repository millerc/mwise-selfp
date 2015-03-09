import os, csv, datetime
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from marketwise.models import Template, TemplateTypePurpose, Customization, CharBlock, TextBlock, ImageBlock 
from marketwise.forms import TemplateFilterForm, TemplateSearchForm, CustomizeTemplateForm


def home(request):
    featured_templates = Template.objects.all().order_by('-rank','?')[:25]
    purposes = TemplateTypePurpose.objects.filter(parent_type__isnull=True)
    template_search_form = TemplateSearchForm()
    return render_to_response("marketwise/home.html", {
        "featured_templates": featured_templates,
        "purposes": purposes,
        "template_search_form": template_search_form,
    }, context_instance=RequestContext(request))

def dashboard(request):
    purposes = TemplateTypePurpose.objects.filter(parent_type__isnull=True)
    template_search_form = TemplateSearchForm()

    return render_to_response("marketwise/dashboard.html", {
        "purposes": purposes,
        "template_search_form": template_search_form,
    }, context_instance=RequestContext(request))

def customization_detail(request, id, template_slug):
    customization = get_object_or_404(Customization, id=id)    
    template = Template.objects.get(slug=customization.template.slug)    
    purposes = TemplateTypePurpose.objects.filter(parent_type__isnull=True)
    template_search_form = TemplateSearchForm()

    return render_to_response("marketwise/customize_detail.html", {
        "customization": customization,
        "template": template,
        "purposes": purposes,
        "template_search_form": template_search_form,
    }, context_instance=RequestContext(request))

def template_detail(request, slug):
    template = get_object_or_404(Template, slug=slug)    
    purposes = TemplateTypePurpose.objects.filter(parent_type__isnull=True)
    template_search_form = TemplateSearchForm()
    
    return render_to_response("marketwise/template_detail.html", {
        "template": template,
        "purposes": purposes,
        "template_search_form": template_search_form,
    }, context_instance=RequestContext(request))

def templates(request, free_templates):
    filtered = False
    purposes = TemplateTypePurpose.objects.filter(parent_type__isnull=True)
    templates = Template.objects.all()
    if free_templates:
        templates = templates.filter(credits_required=0)
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']        
        template_query = get_query(query_string, ['name', 'description', 'keywords',])
        templates = templates.filter(template_query)
        filtered = True
    if request.GET.get('colors'):
        templates = templates.filter(templateclassification__templateclassificationcolor__color__in=list(request.GET.getlist('colors')))
        filtered = True
    if request.GET.get('formats'):
        templates = templates.filter(templateclassification__templateclassificationformat__format__in=list(request.GET.getlist('formats')))
        filtered = True

    templates = templates.distinct().order_by('-rank')
    template_filter_form = TemplateFilterForm(request.GET)
    template_search_form = TemplateSearchForm(request.GET)
    paginator = Paginator(templates, 15)

    page = request.GET.get('page') or 1

    try:
        pager = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pager = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pager = paginator.page(paginator.num_pages)
    
    #templates = pager
    return render_to_response("marketwise/template_list.html", {
        "filtered": filtered,
        "templates": templates,
        "pager": pager,
        "purposes": purposes,
        "free_templates": free_templates,
        "template_filter_form": template_filter_form,
        "template_search_form": template_search_form,
    }, context_instance=RequestContext(request))

def templates_by_purpose(request, slug, parent_slug):
    filtered = False
    purposes = TemplateTypePurpose.objects.filter(parent_type__isnull=True)
    purpose = TemplateTypePurpose.objects.get(slug=slug)
    templates = Template.objects.filter(templateclassification__templateclassificationpurpose__purpose=purpose)
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']        
        template_query = get_query(query_string, ['name', 'description', 'keywords',])
        templates = templates.filter(template_query)
        filtered = True
    if request.GET.get('colors'):
        templates = templates.filter(templateclassification__templateclassificationcolor__color__in=list(request.GET.getlist('colors')))
        filtered = True
    if request.GET.get('formats'):
        templates = templates.filter(templateclassification__templateclassificationformat__format__in=list(request.GET.getlist('formats')))
        filtered = True
        
    templates = templates.distinct().order_by('-rank')
    paginator = Paginator(templates, 15)
    template_filter_form = TemplateFilterForm(request.GET)
    template_search_form = TemplateSearchForm(request.GET)

    page = request.GET.get('page') or 1

    try:
        pager = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pager = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pager = paginator.page(paginator.num_pages)
    
    return render_to_response("marketwise/templatetypepurpose_detail.html", {
        "filtered": filtered,
        "templates": templates,
        "pager": pager,
        "purposes": purposes,
        "purpose": purpose,
        "template_filter_form": template_filter_form,
        "template_search_form": template_search_form,
    }, context_instance=RequestContext(request))
    
from marketwise.search import get_query

def template_search(request):
    query_string = ''
    templates = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        
        template_query = get_query(query_string, ['name', 'description', 'keywords',])
        
        templates = Template.objects.filter(template_query).order_by('-rank')

    paginator = Paginator(templates, 15)

    page = request.GET.get('page') or 1

    try:
        pager = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pager = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pager = paginator.page(paginator.num_pages)

    return render_to_response('marketwise/template_list.html', {
        'query_string': query_string, 
        'templates': templates, 
        'pager': pager, 
    }, context_instance=RequestContext(request))

def template_customize(request, slug):
    template = get_object_or_404(Template, slug=slug)
    purposes = TemplateTypePurpose.objects.filter(parent_type__isnull=True)
    form = CustomizeTemplateForm(template, request)
    testdict = {}
    if request.method == 'POST':
        form = CustomizeTemplateForm(template, request, request.POST, request.FILES)
        if form.is_valid():
            blocks = template.templateblock_set.all()
            customization = Customization(user=request.user, template=template)
            cz = customization.save()
            testdict = {}
            for b in blocks:
                testdict[b.label] = request.POST.get(b.label)
                try:
                    b.templatecharblock
                except:
                    pass
                else:
                    newblock = CharBlock(customization=customization,template_block=b,content=request.POST.get(b.label))
                    newblock.save()
                try:
                    b.templatetextblock
                except:
                    pass
                else:
                    newblock = TextBlock(customization=customization,template_block=b,content=request.POST.get(b.label))
                    newblock.save()
                try:
                    b.templateimageblock
                except:
                    pass
                else:
                    newblock = ImageBlock(customization=customization,template_block=b,content=request.FILES.get(b.label))
                    newblock.save()
            return redirect(customization)
            
    
    return render_to_response('marketwise/template_customize.html', {
        'template': template,
        'form': form,
        'purposes': purposes,
        'testdict': testdict,
    }, context_instance=RequestContext(request))

