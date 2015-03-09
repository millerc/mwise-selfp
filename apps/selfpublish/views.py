# -*- coding: utf-8 -*-
from __future__ import with_statement

import os, csv, datetime, urllib, urllib2

try:
    import json
except ImportError:
    import simplejson as json 

from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.sites.models import Site
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.template.defaultfilters import slugify
from django.db.models import Max, Sum
from selfpublish.models import *
from selfpublish.forms import *

from qbms.views import checkout

def home(request):
    featured_themes = Theme.objects.exclude(id=22).order_by('-rank')[:21]
    return render_to_response("selfpublish/home.html", {
        "featured_themes": featured_themes,        
    }, context_instance=RequestContext(request))

def theme_detail(request, id):
    theme = get_object_or_404(Theme, id=id)
    featured_themes = Theme.objects.exclude(id=22).order_by('-rank')[:21]
    related_themes = Theme.objects.filter(coverdesign__template=theme.coverdesign.template).exclude(id=id)
    return render_to_response("selfpublish/theme_detail.html", {
        "theme": theme,        
        "featured_themes": featured_themes,
        "related_themes": related_themes,        
    }, context_instance=RequestContext(request))

def theme_browse(request):
    themes = Theme.objects.exclude(id=22).order_by('-rank')
    return render_to_response("selfpublish/theme_browse.html", {
        "themes": themes,
    }, context_instance=RequestContext(request))
    
@login_required
def theme_select_membership(request, id):
    theme = get_object_or_404(Theme, id=id)
    current_site = Site.objects.get_current()
    if request.method == 'POST':
        form = MembershipSelectForm(request.POST)
        bycompare = ''
        next = ''
        pub = ''
        if form.is_valid():
            pagecount = form.cleaned_data['membership']
            if 'next' in request.POST:
                next = request.POST['next']
                pub = Publication(title='Untitled Publication',page_count=pagecount,theme=theme,owner=request.user) #Create a new publication instance
                pub.save()
            if 'bycompare' in request.POST:
                bycompare = request.POST['bycompare']
            return render_to_response("selfpublish/theme_select_pagecount.html", {
                "next": next,
                "pub": pub,
                "bycompare": bycompare,
                "theme": theme,
                "pagecount": pagecount,
                "current_site": current_site,
            }, context_instance=RequestContext(request))
        else:
	        form = MembershipSelectForm()
	        return render_to_response("selfpublish/theme_select_membership.html", {
	            "theme": theme,
	            "form": form,        
	        }, context_instance=RequestContext(request))
    else:
        form = MembershipSelectForm()
        return render_to_response("selfpublish/theme_select_membership.html", {
            "theme": theme,
            "form": form,        
        }, context_instance=RequestContext(request))

@login_required
def pagecount_compare(request, id):
    theme = get_object_or_404(Theme, id=id)
    pagecounts = PageCount.objects.exclude(page_count=8)
    return render_to_response("selfpublish/pagecount_compare.html", {
        "theme": theme,
        "pagecounts": pagecounts,
    }, context_instance=RequestContext(request))

@login_required    
def publication_setup(request, setup_key):
    publication = get_object_or_404(Publication, setup_key=setup_key)

    if publication.owner != request.user:
        messages.error(request, 'Requested publication does not belong to currently logged in user.')
        return redirect(dashboard_home)

    if publication.setup_done:
       	messages.info(request, 'Setup for this publication has already been completed.')
        return redirect(publication) #Set was already completed redirect to the publication detail page.
        
    form = PublicationSetupForm()
    theme = publication.theme
    if request.method == 'POST':
        form = PublicationSetupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['decrypted_key'] == publication.page_count.decrypted_key:
                cover = Cover(publication=publication,cover_template=theme.coverdesign.template) #Create a new cover instance
                cover.save() #Save cover
                for block in theme.coverdesign.template.templateblock_set.all(): #Loop through cover template blocks, create and save each one
                    if hasattr(block,'templatecharblock'):
                        cb = CharBlock(template_char_block=block.templatecharblock,layout=cover)
                        cb.save()
                    if hasattr(block,'templateimageblock'):
                        ib = ImageBlock(template_image_block=block.templateimageblock,layout=cover)
                        ib.save()
                    if hasattr(block,'templatefileblock'):
                        fb = FileBlock(template_file_block=block.templatefileblock,layout=cover)
                        fb.save()
                mappings = SpreadTypeMap.objects.filter(page_count=publication.page_count) #Get the default spreads by page count of new publication
                for mapping in mappings:
                    spread = Spread(publication=publication,sequence=mapping.sequence,spread_template=mapping.default_template)
                    spread.save()
                    for block in mapping.default_template.spreadtemplate.template_ptr.templateblock_set.all():
                        if hasattr(block,'templatecharblock'):
                            cb = CharBlock(template_char_block=block.templatecharblock,layout=spread)
                            cb.save()
                        if hasattr(block,'templateimageblock'):
                            ib = ImageBlock(template_image_block=block.templateimageblock,layout=spread)
                            ib.save()
                        if hasattr(block,'templatefileblock'):
                            fb = FileBlock(template_file_block=block.templatefileblock,layout=spread)
                            fb.save()
                        if hasattr(block,'templateadblock'):
                            ab = AdBlock(template_ad_block=block.templateadblock,layout=spread)
                            if spread.sequence == 1:
                                if block.sequence == 1:
                                    pl = AdPriceLevel.objects.get(code='IFC')
                                elif block.sequence == 2:
                                    pl = AdPriceLevel.objects.get(code='IFF')
                            elif spread.sequence == publication.page_count.page_count / 4:
                                pl = AdPriceLevel.objects.get(code='CP')
                            elif spread.sequence == publication.page_count.page_count / 2 - 1:
                                pl = AdPriceLevel.objects.get(code='IBC')
                            elif spread.sequence == publication.page_count.page_count / 2:
                                pl = AdPriceLevel.objects.get(code='OBC')
                            else:
                                pl = AdPriceLevel.objects.get(code='FP')
                            ab.ad_price_level = pl
                            ab.save()
                            
                publication.title = form.cleaned_data['title']
                publication.setup_done = True
                publication.save()
                messages.success(request, 'Publication setup was completed successfully.')
                return redirect(publication)
            else:
                messages.error(request, '%s is not a valid key' % form.cleaned_data['decrypted_key'])
    return render_to_response("selfpublish/publication_setup.html", {
        "form": form,
    }, context_instance=RequestContext(request))

@login_required
def publication_detail(request, id):
    publication = get_object_or_404(Publication, id=id)
    if publication.owner != request.user:
        return HttpResponseForbidden("<h1>Hey, this publication doesn't belong to you!</h1> <p><a href=\"/self-publish/\">Get your own Out of the Box publication.</a></p>")
    return render_to_response("selfpublish/publication_detail.html", {
        "publication": publication,
    }, context_instance=RequestContext(request))
    
@login_required
def layout_detail_old(request, publication_id, layout_id):
    layout = get_object_or_404(Layout, id=layout_id)
    publication = get_object_or_404(Publication, id=publication_id)
    return render_to_response("selfpublish/layout_detail.html", {
        "layout": layout,
        "publication": publication,
    }, context_instance=RequestContext(request))

@login_required
def layout_detail(request, publication_id, layout_id):
    layout = get_object_or_404(Layout, id=layout_id)
    publication = get_object_or_404(Publication, id=publication_id)

    if publication.owner != request.user:
        return HttpResponseForbidden("<h1>Hey, this publication doesn't belong to you!</h1> <p><a href=\"/self-publish/\">Get your own Out of the Box publication.</a></p>")

    if layout.get_publication() != publication:
        return HttpResponseForbidden("<h1>Request mismatch</h1> <p>The layout does not match the publication</p>")
        
    block_list = []
    error_list = []
    
    if request.method == 'POST':
        for block in layout.block_set.all():
            if block.filled == False:
                f = BlockForm(block, request.POST, request.FILES, prefix=str(block.id), label_suffix="")
                if f.is_valid():
                    if hasattr(block,'charblock'):
                        if f.cleaned_data.get(block.template_block.type.label,None):
                            block.charblock.content = f.cleaned_data.get(block.template_block.type.label,None)
                            block.charblock.save()
                            block.filled=True
                            messages.success(request, '<a href="#block%s">%s</a> (%s) saved.' % (block.template_block.sequence, block, block.template_block.sequence))
                    if hasattr(block,'fileblock'):
                        if f.cleaned_data.get('uploadedfile',None):
                            file = File.objects.create(content=f.cleaned_data.get('uploadedfile',None),
                                                       byline=f.cleaned_data.get('byline',None),
                                                       user=block.layout.get_publication().owner
                                                       )
                            block.fileblock.file = file
                            block.fileblock.save()
                            block.filled=True
                            messages.success(request, '<a href="#block%s">%s</a> (%s) saved.' % (block.template_block.sequence, block, block.template_block.sequence))
                    if hasattr(block,'imageblock'):
                        if f.cleaned_data.get('uploadedimage',None):
                            image = Image.objects.create(content=f.cleaned_data.get('uploadedimage',None),
                                                         credit=f.cleaned_data.get('credit',None),
                                                         user=block.layout.get_publication().owner
                                                         )
                            block.imageblock.image = image
                            block.imageblock.caption = f.cleaned_data.get('caption',None)
                            block.imageblock.save()
                            block.filled=True
                            messages.success(request, '<a href="#block%s">%s</a> (%s) saved.' % (block.template_block.sequence, block, block.template_block.sequence))
                else: #Form is not valid
                    for field, errors in f.errors.items():
                        for e in errors:
                            messages.error(request, '%s (%s): %s<br /><a href="#block%s"><em>Go to item</em></a>' % (block, block.template_block.sequence, e, block.template_block.sequence))
                block_list.append({'block': block, 'form': f})
            else:
                block_list.append({'block': block, 'form': 'filled'})
    
    else:
        for block in layout.block_set.all():
            f = BlockForm(block, prefix=str(block.id), label_suffix="")
            block_list.append({'block': block, 'form': f})

    return render_to_response("selfpublish/layout_detail.html", {
        "layout": layout,
        "publication": publication,
        "block_list": block_list,
        "error_list": error_list,
    }, context_instance=RequestContext(request))

@login_required    
def change_layout(request, publication_id, layout_id):
    publication = get_object_or_404(Publication, id=publication_id)
    
    if publication.owner != request.user:
        return HttpResponseForbidden("<h1>Hey, this publication doesn't belong to you!</h1> <p><a href=\"/self-publish/\">Get your own Out of the Box publication.</a></p>")
    
    current_layout = get_object_or_404(Layout, id=layout_id)

    if current_layout.get_publication() != publication:
        return HttpResponseForbidden("<h1>Request mismatch</h1> <p>The layout does not match the publication</p>")
        
    if hasattr(current_layout, 'spread'):
        current_design = current_layout.spread.design()
        available_designs = SpreadDesign.objects.filter(
                                                        theme=current_layout.get_publication().theme,
                                                        template__type=current_layout.spread.spread_template.type).exclude(pk=current_layout.spread.design().pk
                                                        )
    elif hasattr(current_layout, 'cover'):
        current_design = publication.theme.coverdesign
        available_designs = CoverDesign.objects.exclude(pk=current_design.pk)

    if request.method == 'POST':
        new_design = Design.objects.get(id=request.POST['new_design'])
        if hasattr(new_design, 'spreaddesign'):
            new_design = SpreadDesign.objects.get(id=request.POST['new_design'])
            new_template = new_design.template
            
        elif hasattr(new_design, 'coverdesign'):
            new_design = CoverDesign.objects.get(id=request.POST['new_design'])
            new_template = new_design.template
            if current_layout.cover.cover_template == new_template: #Same template. Only the theme is changing.
                publication.theme = new_design.theme
                publication.save()
                return redirect(current_layout)
        
        if current_layout.block_set.filter(filled=True).count() == 0: #No blocks filled; just change layouts
            if hasattr(current_layout, 'spread'): #Is this a spread?
                current_layout.spread.spread_template = new_template #Set the new template for this spread
                current_layout.spread.save() #Save spread
            if hasattr(current_layout, 'cover'): #Or is it a cover?
                current_layout.cover.cover_template = new_template #Set the new template for this cover
                current_layout.cover.save() #Save cover
                publication.theme = new_design.theme #Set new theme for this publication
                publication.save() #Save publication
            for b in new_template.template_ptr.templateblock_set.all(): #Loop through template blocks and create new blocks for this layout
                if hasattr(b,'templatecharblock'):
                    cb = CharBlock(template_char_block=b.templatecharblock,layout=current_layout)
                    cb.save()
                if hasattr(b,'templateimageblock'):
                    ib = ImageBlock(template_image_block=b.templateimageblock,layout=current_layout)
                    ib.save()
                if hasattr(b,'templatefileblock'):
                    fb = FileBlock(template_file_block=b.templatefileblock,layout=current_layout)
                    fb.save()

            current_layout.block_set.exclude(template_block__template=new_template).delete() #Delete the blocks not associated with the new template
            return redirect(current_layout)

        #At least one block is filled; Map existing content to new layout
        
        dropped_blocks = set() #Blocks that will not be used in new layout
        resolve_blocks = set() #Blocks that will need user input to map to new layout
        mapped_blocks = set() #Blocks that can be mapped to a single block in new layout
        
        for b in current_layout.block_set.filter(filled=True):
        
            if current_layout.block_set.filter(filled=True,template_block__type=b.template_block.type).count() > 1: #Is there more than one filled block of the same type?
                resolve_blocks.add(b.pk) #Yes, store this block to be resolved by user
            else:
                try:
                    new_template.templateblock_set.get(type=b.template_block.type)
                except TemplateBlock.DoesNotExist:
                    dropped_blocks.add(b.pk) #No blocks of this type exist in the new layout. Drop the block.
                except TemplateBlock.MultipleObjectsReturned:
                    resolve_blocks.add(b.pk) #Store this block to be resolved by User
                else:
                    mapped_blocks.add(b.pk) #Move this block to the new layout
        dropped_blocks = Block.objects.filter(pk__in=dropped_blocks)
        mapped_blocks = Block.objects.filter(pk__in=mapped_blocks)
        resolve_blocks = Block.objects.filter(pk__in=resolve_blocks)
        conflict_form = BlockConflictForm(resolve_blocks,new_design)
        
        if 'confirm' in request.POST: #if request came from confirmation page, proceed to create and map blocks
            conflict_form = BlockConflictForm(resolve_blocks,new_design,request.POST)
            if conflict_form.is_valid():
                if hasattr(current_layout, 'spread'):
                    current_layout.spread.spread_template = new_template
                    current_layout.spread.save()
                if hasattr(current_layout, 'cover'):
                    current_layout.cover.cover_template = new_template
                    current_layout.cover.save()
                    publication.theme = new_design.theme
                    publication.save()
                new_blocks = set()
                for b in new_template.template_ptr.templateblock_set.all():
                    if hasattr(b,'templatecharblock'):
                        cb = CharBlock(template_char_block=b.templatecharblock,layout=current_layout)
                        cb.save()
                        new_blocks.add(cb.pk)
                    if hasattr(b,'templateimageblock'):
                        ib = ImageBlock(template_image_block=b.templateimageblock,layout=current_layout)
                        ib.save()
                        new_blocks.add(ib.pk)
                    if hasattr(b,'templatefileblock'):
                        fb = FileBlock(template_file_block=b.templatefileblock,layout=current_layout)
                        fb.save()
                        new_blocks.add(fb.pk)
                
                new_blocks = Block.objects.filter(pk__in=new_blocks)
                    
                for b in mapped_blocks:
                    new_block = new_blocks.get(template_block__type=b.template_block.type)
                    if hasattr(b, 'charblock'):
                        new_block.charblock.content = b.charblock.content
                        new_block.charblock.save()
                    if hasattr(b, 'imageblock'):
                        new_block.imageblock.image = b.imageblock.image
                        new_block.imageblock.save()
                    if hasattr(b, 'fileblock'):
                        new_block.fileblock.file = b.fileblock.file
                        new_block.fileblock.save()
                for b in resolve_blocks:
                    if conflict_form.cleaned_data['b'+str(b.pk)]:
                        new_block = new_blocks.get(template_block=conflict_form.cleaned_data['b'+str(b.pk)])
                        if hasattr(b, 'charblock'):
                            new_block.charblock.content = b.charblock.content
                            new_block.charblock.save()
                        if hasattr(b, 'imageblock'):
                            new_block.imageblock.image = b.imageblock.image
                            new_block.imageblock.save()
                        if hasattr(b, 'fileblock'):
                            new_block.fileblock.file = b.fileblock.file
                            new_block.fileblock.save()
                current_layout.block_set.exclude(template_block__template=new_template).delete()
                return redirect(current_layout)
                
        return render_to_response("selfpublish/layout_change_confirm.html", {
            "current_layout": current_layout,
            "current_design": current_design,
            "publication": publication,
            "new_template": new_template,
            "new_design": new_design,
            "dropped_blocks": dropped_blocks,
            "mapped_blocks": mapped_blocks,
            "resolve_blocks": resolve_blocks,
            "conflict_form": conflict_form,
        }, context_instance=RequestContext(request))

    return render_to_response("selfpublish/layout_change.html", {
        "current_layout": current_layout,
        "current_design": current_design,
        "available_designs": available_designs,
        "publication": publication,
    }, context_instance=RequestContext(request))

@login_required    
def change_layout_execute(request, publication_id, layout_id):
    publication = get_object_or_404(Publication, id=publication_id)
    
    if publication.owner != request.user:
        return HttpResponseForbidden("<h1>Hey, this publication doesn't belong to you!</h1> <p><a href=\"/self-publish/\">Get your own Out of the Box publication.</a></p>")
    
    old_layout = get_object_or_404(Layout, id=layout_id)
    
    if old_layout.get_publication() != publication:
        return HttpResponseForbidden("<h1>Request mismatch</h1> <p>The layout does not match the publication</p>")        
    
    if request.method == 'POST':
        new_template = Template.objects.get(id=request.POST['new_template'])
        f = BlockConflictForm(block_conflicts,new_template,request.POST)
        if f.is_valid():
            new_template = f.cleaned_data['new_template']
            if hasattr(new_template, "spreadtemplate"):
                new_layout = Spread(publication=publication,spread_template=new_template.spreadtemplate,sequence=old_layout.spread.sequence)
            if hasattr(new_template, "covertemplate"):
                new_layout = Cover(publication=publication,cover_template=newtemplate.covertemplate)
            new_layout.save()
            for b in new_template.templateblock_set.all():
                if hasattr(block,'templatecharblock'):
                    cb = CharBlock(template_char_block=block.templatecharblock,layout=new_layout)
                    cb.save()
                if hasattr(block,'templateimageblock'):
                    ib = ImageBlock(template_image_block=block.templateimageblock,layout=new_layout)
                    ib.save()
                if hasattr(block,'templatefileblock'):
                    fb = FileBlock(template_file_block=block.templatefileblock,layout=new_layout)
                    fb.save()
            
            for b in old_layout.block_set.filter(filled=True): #Loop through filled blocks on old layout and attempt to find suitable match on new layout
                if old_layout.block_set.filter(filled=True,template_block__type=b.template_block.type).count() > 1: #Is there more than one filled block of the same type?
                    if f.cleaned_data[b]:
                        new_block = new_layout.block_set.get(template_block=f.cleaned_data[b]) 
                else:
                    try:
                        new_block = newlayout.block_set.get(template_block__type=b.template_block.type)
                    except Block.DoesNotExist:
                        continue #Nothing to map, end this iteration
                    except Block.MultipleObjectsReturned:
                        if f.cleaned_data[b]:
                            new_block = new_layout.block_set.get(template_block=f.cleaned_data[b])
                    else:
                        new_block = newlayout.block_set.get(template_block__type=b.template_block.type)
                if hasattr(b, 'charblock'):
                    new_block.charblock.content = b.charblock.content
                if hasattr(b, 'imageblock'):
                    new_block.imageblock.image.content = b.imageblock.image.content
                if hasattr(b, 'fileblock'):
                    new_block.imageblock.file.content = b.fileblock.file.content
                new_block.save()
            old_layout.delete()
            return redirect(new_layout)
        return render_to_response("selfpublish/layout_change_confirm.html", {
            #"current_layout": current_layout,
            #"current_design": current_design,
            "publication": publication,
            #"new_template": new_template,
            #"new_design": new_design,
            #"dropped_blocks": dropped_blocks,
            #"mapped_blocks": mapped_blocks,
            #"resolve_blocks": resolve_blocks,
            "conflict_form": f,
        }, context_instance=RequestContext(request))
    return redirect(selfpublish_home)        

@login_required
def block_detail(request, publication_id, layout_id, block_id):
    form = ImageFilterForm()
    publication = get_object_or_404(Publication, id=publication_id)
    
    if publication.owner != request.user:
        return HttpResponseForbidden("<h1>Hey, this publication doesn't belong to you!</h1> <p><a href=\"/self-publish/\">Get your own Out of the Box publication.</a></p>")

    layout = get_object_or_404(Layout, id=layout_id)
    block = get_object_or_404(Block, id=block_id)
    
    if block.layout != layout or layout.get_publication() != publication:
        return HttpResponseForbidden("<h1>Request mismatch</h1> <p>Either the block does match the layout or the layout does not match the publication</p>")
        
    f = BlockForm(block)

    if request.method == 'POST':
        credit = ''
        f = BlockForm(block, request.POST, request.FILES)
        if f.is_valid():
            if hasattr(block,'charblock'):
                block.charblock.content = f.cleaned_data[block.template_block.type.label]
                block.charblock.save()
            if hasattr(block,'fileblock'):
                if f.cleaned_data['uploadedfile']:
                    file = File.objects.create(content=f.cleaned_data['uploadedfile'],
                                               byline=f.cleaned_data['byline'],
                                               user=block.layout.get_publication().owner
                                               )
                    block.fileblock.file = file
                    block.fileblock.save()
                    block.filled = True
            if hasattr(block,'imageblock'):
                if f.cleaned_data['uploadedimage']:
                    image = Image.objects.create(content=f.cleaned_data['uploadedimage'],
                                                 credit=f.cleaned_data['credit'],
                                                 caption=f.cleaned_data['caption'],
                                                 user=block.layout.get_publication().owner
                                                 )
                    block.imageblock.image = image
                    block.imageblock.caption = f.cleaned_data['caption']
                else:
                    if block.imageblock.image:
                       block.imageblock.image.credit = f.cleaned_data['credit']
                       block.imageblock.caption = f.cleaned_data['caption']
                block.imageblock.image.save()
                block.imageblock.save()
                block.filled = True
                
            messages.success(request, '<a href="#block%s">%s</a> (%s) saved.' % (block.template_block.sequence, block, block.template_block.sequence))
            return redirect(layout)
            
        else: #Form is not valid
            for field, errors in f.errors.items():
                for e in errors:
                    messages.error(request, '%s (%s): %s<br /><a href="#block%s"><em>Go to item</em></a>' % (block, block.template_block.sequence, e, block.template_block.sequence))

    return render_to_response("selfpublish/block_detail.html", {
        "f":f,
        "b": block,
        "layout": layout,
        "publication": publication,
    }, context_instance=RequestContext(request))
        
@login_required
def media_select(request, block_id, layout_id, publication_id):
    block = get_object_or_404(Block, id=block_id)
    layout = block.layout
    publication = layout.get_publication()
    
    if publication.owner != request.user:
        return HttpResponseForbidden("<h1>Hey, this publication doesn't belong to you!</h1> <p><a href=\"/self-publish/\">Get your own Out of the Box publication.</a></p>")
    
    if block.layout != layout or layout.get_publication() != publication:
        return HttpResponseForbidden("<h1>Request mismatch</h1> <p>Either the block does match the layout or the layout does not match the publication</p>")
        
    fileblock = None
    files = None
    imageblock = None
    images = None
    
    if hasattr(block, 'imageblock'):
        imageblock = block.imageblock
        form = ImageFilterForm()
        if request.method == 'POST':
            image = Image.objects.get(pk=request.POST['image_id'])
            imageblock.image = image
            imageblock.save()
            return redirect(block)
        if request.method == 'GET':
            form = ImageFilterForm(request.GET)
            if form.is_valid():
                if form.cleaned_data['filter']:
                    images = Image.objects.filter(categories=form.cleaned_data['filter'])
                else:
                    images = Image.objects.filter(user=publication.owner) 
        else:
            images = Image.objects.filter(user=publication.owner)
           
    if hasattr(block, 'fileblock'):
        fileblock = block.fileblock
        form = None
        if request.method == 'POST':
            file = File.objects.get(pk=request.POST['file_id'])
            fileblock.file = file
            fileblock.save()
            return redirect(block)
        files = File.objects.filter(user=publication.owner)
            
    return render_to_response("selfpublish/media_select.html", {
        "fileblock": fileblock,
        "imageblock": imageblock,
        "layout": layout,
        "publication": publication,
        "form": form,
        "files": files,
        "images":images,
    }, context_instance=RequestContext(request))    

######################
# SALES ENGINE VIEWS #
######################

def sales_home(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)
    leads = {
             'new':publication.lead_set.filter(status__isnull=True),
             'pending':publication.lead_set.filter(status__description__iexact='pending'),
             'sold':publication.lead_set.filter(status__description__iexact='sold'),
             'declined':publication.lead_set.filter(status__description__iexact='declined')
            }
    status = {
              'pending':LeadStatusType.objects.get(description__iexact='pending'),
              'sold':LeadStatusType.objects.get(description__iexact='sold'),
              'declined':LeadStatusType.objects.get(description__iexact='declined'),
              }
    adblocks = AdBlock.objects.filter(layout__in=publication.spread_set.all()).order_by('-price')
    lineads = LineAd.objects.filter(publication=publication)
    return render_to_response("selfpublish/sales_home.html", {
        "publication": publication,
        "leads": leads,
        "status": status,
        "adblocks": adblocks,
        "lineads": lineads
    }, context_instance=RequestContext(request))

def lead_list(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)
    leads = Lead.objects.filter(publication=publication)
    form = LeadSearchForm()
    if request.method == 'GET':
        form = LeadSearchForm(request.GET)
        if form.is_valid():
            if form.cleaned_data['search']:
                search_terms = form.cleaned_data['search'].split()
                queries = [Q(organization__icontains=search_term)|Q(contact_name__icontains=search_term) for search_term in search_terms]
                query = queries.pop()
                for item in queries:
                    query |= item
                leads = leads.filter(query)
            if form.cleaned_data['status']:
                leads = leads.filter(status=form.cleaned_data['status'])
    paginator = Paginator(leads, 20)
    page = request.GET.get('page', 1)
    pager = paginator.page(page)
    leads = pager.object_list
    
    queries_without_page = request.GET.copy()
    if queries_without_page.has_key('page'):
        del queries_without_page['page']
    request.session['previous_get'] = request.GET.copy()

    return render_to_response("selfpublish/sales_lead_list.html", {
        "publication": publication,
        "leads": leads,
        "form": form,
        "pager": pager,
        "queries": queries_without_page,
    }, context_instance=RequestContext(request))
    
def lead_add(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)
    new_lead = Lead(publication=publication)
    form = LeadEditForm(instance=new_lead)
    if request.method == 'POST':
        form = LeadEditForm(request.POST, instance=new_lead)
        if form.is_valid():
            new_lead = form.save()
            messages.success(request, "Lead added successfully.")
            if request.POST.get('save_continue',''):
                return redirect(new_lead)
            else:
                return redirect(lead_list,publication_id=publication.id)
        else:
            messages.error(request, "See below for detail.")
    return render_to_response("selfpublish/sales_lead_detail.html", {
        "publication": publication,
        "new_lead": new_lead,
        "form": form,
    }, context_instance=RequestContext(request))
        
def orderize(order_items):
    order_dict = {'Items': [], 'EstDeliveryDate': '12/21/2012'}
    for item in order_items:
        sku = 'P%sA%s' % (item.publication.id, item.id)
        desc = item.__unicode__()
        if hasattr(item, 'displayad'):
            price = item.displayad.adblock.price
        else:
            price = item.publication.listing_price
        order_dict['Items'].append({'ItemSku': sku, 'ItemDesc': desc, 'ItemPrice': str(price), 'ItemQty': '1', 'ItemIsShippable': '0', 'ItemIsTaxable': '0'})
    return json.dumps(order_dict)


def send_invite(lead):
    current_site = Site.objects.get_current()
    plaintext = get_template('selfpublish/sales_invite_email.txt')
    htmly = get_template('selfpublish/sales_invite_email.html')
    d = Context({ 'lead': lead, 'current_site': current_site })
    subject, from_email, to = lead.publication, lead.publication.owner.email, lead.email
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def lead_detail(request, publication_id, lead_id):
    current_site = Site.objects.get_current()
    publication = get_object_or_404(Publication, id=publication_id)
    lead = get_object_or_404(Lead, id=lead_id)
    line_ads = LineAd.objects.filter(lead=lead)
    display_ads = DisplayAd.objects.filter(lead=lead)
    form = LeadEditForm(instance=lead)
    adblocks = AdBlock.objects.filter(layout__in=publication.spread_set.all(),display_ad__isnull=True)
    aform = DisplayAdReservationForm(adblocks)
    amount_due = line_ads.exclude(paid=True).count() * publication.listing_price + (display_ads.exclude(paid=True).aggregate(Sum('adblock__price'))['adblock__price__sum'] or 0)

    if request.method == 'POST' and request.POST.get('status',''):
        try:
            lead.status = LeadStatusType.objects.get(slug=request.POST.get('status',''))
        except:
            lead.status = None
        lead.save()
        messages.success(request, 'Lead status updated.')
        return redirect(lead)
        
    if request.method == 'POST' and request.POST.get('invite',''):
        send_invite(lead)
        messages.success(request, 'Invitation sent to %s' % lead.email)
        return redirect(lead)        

    if request.method == 'POST' and request.POST.get('reserve-display',''):
        aform = DisplayAdReservationForm(adblocks, request.POST)
        if aform.is_valid():
            new_display = DisplayAd(publication=publication,lead=lead)
            new_display.save()
            adblock = aform.cleaned_data['adspace']
            adblock.display_ad = new_display
            adblock.save()
            if aform.cleaned_data['listing']:
                new_listing = LineAd(publication=publication,lead=lead)
                new_listing.save()
            else:
                new_listing = None
            messages.success(request,'Reservation recorded. Process payment to complete transaction')
            return redirect(lead)

    if request.method == 'POST' and request.POST.get('reserve-listing',''):
        new_listing = LineAd(publication=publication,lead=lead)
        new_listing.save()
        messages.success(request,'Reservation recorded. Process payment to complete transaction')
        return redirect(lead)

    if request.method == 'POST' and request.POST.get('cancel-reservation',''):
        ad = Ad(id=request.POST.get('cancel-reservation',''),lead=lead)
        ad.delete()
        messages.success(request,'Reservation cancelled.')
        return redirect(lead)

    if request.method == 'POST' and request.POST.get('paypage',''):
        order_items = Ad.objects.filter(lead=lead,paid=False)
        order = orderize(order_items)
        user_data = str(lead.id)+';'+','.join(str(item.id) for item in order_items)
        comment = 'Thank you for your support of the %s.' % publication.title
        cancel_url = request.build_absolute_uri()
        checkout_url = checkout(amount_due, order, user_data, lead.organization, str(lead.id), comment, cancel_url)
        return redirect(checkout_url)

    if request.method == 'POST':
        form = LeadEditForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, "Lead saved successfully.")
            if request.POST.get('save',''):
                list_last_get = reverse(lead_list,kwargs={'publication_id':publication.id})+'?'+request.session['previous_get'].urlencode()
                return redirect(list_last_get)
        else:
            messages.error(request, "See below for detail.")
        
    return render_to_response("selfpublish/sales_lead_detail.html", {
        "publication": publication,
        "lead": lead,
        "form": form,
        "aform": aform,
        "line_ads": line_ads,
        "display_ads": display_ads,
        "amount_due": amount_due
    }, context_instance=RequestContext(request))

def lead_import(request,publication_id):
    publication = get_object_or_404(Publication, id=publication_id)
    form = LeadImportForm()
    new_leads = []
    import_fields = ''
    path = ''
    if request.method == 'POST':
        if request.POST.get('upload',''):
            form = LeadImportForm(request.POST, request.FILES)
            if form.is_valid():
                import_file = request.FILES['file']
                path = default_storage.save('selfpublish/tmp/leads/%s/%s' % (publication.id, import_file.name), ContentFile(import_file.read()))

                with open(os.path.join(settings.MEDIA_ROOT, path), 'rb') as f:
                    import_fields = filter(None,csv.reader(f).next())
                with open(os.path.join(settings.MEDIA_ROOT, path), 'rb') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        new_leads.append(row)
                form = LeadImportMapForm(import_fields)
        elif request.POST.get('next',''):
            path = request.POST.get('path','')
            with open(os.path.join(settings.MEDIA_ROOT, path), 'rb') as f:
                reader = csv.reader(f)
                import_fields = filter(None,reader.next())
            form = LeadImportMapForm(import_fields, request.POST)
            if form.is_valid():
               with open(os.path.join(settings.MEDIA_ROOT, path), 'rb') as f:
                   reader = csv.DictReader(f)
                   for row in reader:
                       lead, _ = Lead.objects.get_or_create(
                                                            organization=row[form.cleaned_data['organization']],
                                                            contact_name=row[form.cleaned_data['contact']],
                                                            publication=publication
                                                            )
                       lead.phone = row.get(form.cleaned_data['phone'],lead.phone) or lead.phone
                       lead.email = row.get(form.cleaned_data['email'],lead.email) or lead.email
                       lead.note = row.get(form.cleaned_data['note'],lead.note) or lead.note
                       lead.publication = publication
                       lead.save()
               return redirect(lead_list, publication_id=publication.id)
            else:
                with open(os.path.join(settings.MEDIA_ROOT, path), 'rb') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        new_leads.append(row)
               
    return render_to_response("selfpublish/sales_lead_import.html", {
        "publication": publication,
        "form": form,
        "new_leads": new_leads,
        "fields": import_fields,
        "path": path,
    }, context_instance=RequestContext(request))

def lead_invite_send(request, publication_id, lead_id):
    lead = get_object_or_404(Lead, id=lead_id)
    current_site = Site.objects.get_current()
    
    plaintext = get_template('selfpublish/sales_invite_email.txt')
    htmly = get_template('selfpublish/sales_invite_email.html')
    
    d = Context({ 'lead': lead, 'current_site': current_site })
    
    subject, from_email, to = lead.publication, lead.publication.owner.email, lead.email
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    lead.save()
    messages.success(request, 'Invitation sent to %s' % lead.email)
    return redirect(lead)

@login_required
def lead_invite_accept(request, invitation_code):
    lead = get_object_or_404(Lead, invitation_code=invitation_code)
    lead.user = request.User
    lead.save()
    return redirect('sponsor_welcome,publication_id=lead.publication.id')

def sponsor_welcome(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)
    
    return render_to_response("selfpublish/sponsor_welcome.html", {
        "publication": publication,
    }, context_instance=RequestContext(request))

def sponsor_display(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)
    display_ads = AdBlock.objects.filter(layout__in=publication.spread_set.all()).order_by('-price')
    return render_to_response("selfpublish/sponsor_display.html", {
        "publication": publication,
        "ads": display_ads,
    }, context_instance=RequestContext(request))
    
def sponsor_listings(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)
    listings_available = publication.page_count.listings - LineAd.objects.filter(publication=publication).count()
    return render_to_response("selfpublish/sponsor_listings.html", {
        "publication": publication,
        "listings_available": listings_available
    }, context_instance=RequestContext(request))

def sponsor_contact(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)
    new_lead = Lead(publication=publication)
    form = LeadEditForm(instance=new_lead)
    if request.method == 'POST':
        form = LeadEditForm(request.POST, instance=new_lead)
        if form.is_valid():
            new_lead = form.save()
            send_mail(
                'Via contact form: %s' % publication.title, 
                'New lead via Out Of The Box Sales Engine contact form.\n\n%s' % new_lead.get_absolute_url(),
                form.cleaned_data.get('email','self-publish@communitylink.com'), 
                [publication.owner.email], 
                fail_silently=False, 
            )
            messages.success(request, "Your message has been sent. Thank You.")
            return redirect(sponsor_welcome,publication_id=publication.id)
    return render_to_response("selfpublish/sponsor_contact.html", {
        "publication": publication,
        "form": form,
    }, context_instance=RequestContext(request))

def reserve_display(request, publication_id, adblock_id):
    publication = get_object_or_404(Publication, id=publication_id)
    adblock = get_object_or_404(AdBlock, id=adblock_id)
    
    if request.method == 'POST':
        if request.POST['confirm_reservation']:
            new_display = DisplayAd(publication=publication, user=request.user)
            new_display.save()
            adblock.display_ad = new_display
            adblock.save()
            
    current_site = Site.objects.get_current()

    return render_to_response("selfpublish/sponsor_display_reserve.html", {
        "publication": publication,
        "adblock": adblock,
        "current_site": current_site,
    }, context_instance=RequestContext(request))

def displayad_setup(request, setup_key):
    displayad = get_object_or_404(DisplayAd, setup_key=setup_key)
    if request.user == displayad.user:
        if displayad.setup_done == False:
            displayad.setup_done = True
            displayad.save()
            return redirect(displayad)
        else:
            messages.error(request, "This transaction has already been completed.")
            return redirect(displayad)
    else:
        messages.error(request, "This premium is not associated with the currently logged in user. Please log in with the account used to reserve the listing and retry the link you received at checkout.")
        return redirect(dashboard_home)

def displayad_detail(request, publication_id, displayad_id):
    publication = get_object_or_404(Publication, id=publication_id)
    displayad = get_object_or_404(DisplayAd, id=displayad_id)
    
    if request.method == 'POST':
        form = DisplayAdForm(request.POST, request.FILES, instance=displayad)
        if form.is_valid():
            form.save()
            messages.success(request, "Content uploaded and saved successfully.")
            return redirect(displayad)
        else:
            messages.error(request, "There was an error processing your file. See details below.")
    else:
        form = DisplayAdForm(instance=displayad)
            
    return render_to_response("selfpublish/displayad_detail.html", {
        "publication": publication,
        "displayad": displayad,
        "form": form,
        }, context_instance=RequestContext(request))
     
@login_required    
def reserve_listing(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)
    
    if request.method == 'POST':
        if request.POST['confirm_reservation']:
            new_listing = LineAd(publication=publication, user=request.user)
            new_listing.save()
    else:
        new_listing = None

    current_site = Site.objects.get_current()
            
    return render_to_response("selfpublish/sponsor_listings_reserve.html", {
        "publication": publication,
        "new_listing": new_listing,
        "current_site": current_site,
    }, context_instance=RequestContext(request))

@login_required
def linead_setup(request, setup_key):
    linead = get_object_or_404(LineAd, setup_key=setup_key)
    if request.user == linead.user:
        if linead.setup_done == False:
            linead.setup_done = True
            linead.save()
            return redirect(linead)
        else:
            messages.error(request, "This transaction has already been completed.")
            return redirect(linead)
    else:
        messages.error(request, "This listing is not associated with the currently logged in user. Please log in with the account used to reserve the listing and retry the link you received at checkout.")
        return redirect(dashboard_home)

@login_required        
def linead_detail(request, publication_id, linead_id):
    publication = get_object_or_404(Publication, id=publication_id)
    linead = get_object_or_404(LineAd, id=linead_id)
    AdLineFormSet = inlineformset_factory(LineAd, AdLine, extra=10, max_num=10, fields=('text',), can_order=True)
    if request.method == "POST":
        form = LineAdForm(request.POST, request.FILES, instance=linead)
        formset = AdLineFormSet(request.POST, instance=linead)
        if formset.is_valid() and form.is_valid():
            form.save()
            formset.save(commit=False)
            for form in formset.ordered_forms:
                form.instance.sequence = form.cleaned_data['ORDER'] or AdLine.objects.filter(line_ad=linead).aggregate(Max('sequence')) + 1
                form.instance.save()
            messages.success(request,"Listing saved.")
            return redirect(linead)
        else:
            messages.error(request, "There was a problem saving. See below for detail.")

    else:
        form = LineAdForm(instance=linead)
        formset = AdLineFormSet(instance=linead)
        
    return render_to_response("selfpublish/linead_detail.html", {
        "publication": publication,
        "linead": linead,
        "form": form,
        "formset": formset,
    }, context_instance=RequestContext(request))

    
     
##############################################    
# None of the following views are being used #
##############################################
    
def block_edit(request, publication_id, layout_id, block_id):
    isvalidform = False
    block = get_object_or_404(Block, id=block_id)
    layout = get_object_or_404(Layout, id=layout_id)
    f = BlockForm(block)
    if request.method == 'POST':
        prefix = str(block.id)+'-'
        f = BlockForm(block, request.POST, request.FILES, prefix=str(block.id))
        if f.is_valid():
            if hasattr(block,'charblock'):
                block.charblock.content = f.cleaned_data.get(block.template_block.type.label,None)
                block.charblock.save()
            if hasattr(block,'fileblock'):
                if f.cleaned_data.get('uploadedfile',None):
                    file = File.objects.create(content=f.cleaned_data.get('uploadedfile',None),
                                               byline=f.cleaned_data.get('byline',None),
                                               user=block.layout.get_publication().owner
                                               )
                    block.fileblock.file = file
                    block.fileblock.save()
                else:
                    block.fileblock.file = f.cleaned_data.get('file',None)
                    if f.cleaned_data.get('file',None):
                        block.fileblock.file.byline = f.cleaned_data('byline',None)
                        block.fileblock.file.save()
                    block.fileblock.save()
            if hasattr(block,'imageblock'):
                if f.cleaned_data.get('uploadedimage',None):
                    image = Image.objects.create(content=f.cleaned_data.get('uploadedimage',None),
                                                 credit=f.cleaned_data.get('credit',None),
                                                 user=block.layout.get_publication().owner
                                                 )
                    block.imageblock.image = image
                    block.imageblock.caption = f.cleaned_data.get('caption',None)
                    block.imageblock.save()
                else:
                    if layout.get_publication().owner == block.imageblock.image.user:
                        block.imageblock.image.credit = f.cleaned_data.get('credit',None)
                        block.imageblock.caption = f.cleaned_data.get('caption',None)
                    block.imageblock.image.save()
                    block.imageblock.save()
            return redirect(layout)
        
def new_publication(title, pagecount, theme, owner):
    pub = Publication(title=title,page_count=pagecount,theme=theme,owner=owner) #Create a new publication instance
    pub.save() #Save new publication
    cover = Cover(publication=pub,cover_template=theme.coverdesign.template) #Create a new cover instance
    cover.save() #Save cover
    for block in theme.coverdesign.template.templateblock_set.all(): #Loop through cover template blocks, create and save each one
        if hasattr(block,'templatecharblock'):
            cb = CharBlock(template_char_block=block.templatecharblock,layout=cover)
            cb.save()
        if hasattr(block,'templateimageblock'):
            ib = ImageBlock(template_image_block=block.templateimageblock,layout=cover)
            ib.save()
        if hasattr(block,'templatefileblock'):
            fb = FileBlock(template_file_block=block.templatefileblock,layout=cover)
            fb.save()
    mappings = SpreadTypeMap.objects.filter(page_count=pagecount) #Get the default spreads by page count of new publication
    for mapping in mappings:
        spread = Spread(publication=pub,sequence=mapping.sequence,spread_template=mapping.default_template)
        spread.save()
        for block in mapping.default_template.spreadtemplate.template_ptr.templateblock_set.all():
            if hasattr(block,'templatecharblock'):
                cb = CharBlock(template_char_block=block.templatecharblock,layout=spread)
                cb.save()
            if hasattr(block,'templateimageblock'):
                ib = ImageBlock(template_image_block=block.templateimageblock,layout=spread)
                ib.save()
            if hasattr(block,'templatefileblock'):
                fb = FileBlock(template_file_block=block.templatefileblock,layout=spread)
                fb.save()

def browse_images(request):
    form = ImageFilterForm()
    if request.method == 'GET':
        form = ImageFilterForm(request.GET)
        if form.is_valid():
            if form.cleaned_data['filter']:
                images = Image.objects.filter(categories=form.cleaned_data['filter'])
            else:
                images = Image.objects.filter(user__username='commlink') 
    else:
        images = Image.objects.filter(user__username='commlink') 
    return render_to_response("selfpublish/image_browse.html", {
        "images":images,
        "form":form,
    }, context_instance=RequestContext(request))    
    
