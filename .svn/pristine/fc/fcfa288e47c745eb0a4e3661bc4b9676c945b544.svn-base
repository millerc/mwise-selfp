# -*- coding: utf-8 -*-
from django.contrib import admin

from selfpublish.models import *

class FileImageAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'user')
    list_filter = ('user',)
    
class ImageAdmin(FileImageAdmin):
    filter_horizontal = ('categories',)
    
class PageCountAdmin(admin.ModelAdmin):
    list_display = ('page_count','minimum_articles','maximum_articles','advertisements','listings','revenue','minimum_membership','maximum_membership')
    list_editable = ('minimum_articles','maximum_articles','advertisements','listings','revenue','minimum_membership','maximum_membership')

class SpreadTypeMapAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'page_count', 'sequence', 'spread_type', 'default_template')
    list_editable = ('page_count', 'sequence', 'spread_type', 'default_template')
    list_filter = ('page_count',)
    
class CoverDesignInline(admin.TabularInline):
    model = CoverDesign
    extra = 0
    
class SpreadDesignInline(admin.TabularInline):
    model = SpreadDesign
    extra = 0

class TemplateCharBlockInline(admin.TabularInline):
    model = TemplateCharBlock
    extra = 0

class TemplateFileBlockInline(admin.TabularInline):
    model = TemplateFileBlock
    extra = 0

class TemplateImageBlockInline(admin.TabularInline):
    model = TemplateImageBlock
    extra = 0

class TemplateAdBlockInline(admin.TabularInline):
    model = TemplateAdBlock
    extra = 0

class ThemeAdmin(admin.ModelAdmin):
    save_as = True
    search_fields = ['name','description','keywords']

class CoverTemplateAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    search_fields = ['name']
    inlines = [
        CoverDesignInline,
        TemplateCharBlockInline,
        TemplateFileBlockInline,
        TemplateImageBlockInline,
        ]

class SpreadTemplateAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    search_fields = ['name']
    inlines = [
        SpreadDesignInline,
        TemplateCharBlockInline,
        TemplateFileBlockInline,
        TemplateImageBlockInline,
        TemplateAdBlockInline,
        ]

class CoverInline(admin.TabularInline):
    model = Cover
    extra = 0
    
class SpreadInline(admin.TabularInline):
    model = Spread
    extra = 0
    
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title','page_count','owner','status','added','updated')
    list_filter = ('page_count','owner','status',)
    search_fields = ['title']
    inlines = [
        CoverInline,
        SpreadInline,
        ]

class CharBlockInline(admin.TabularInline):
    model = CharBlock
    exclude = ('template_block','filled',)
    raw_id_fields = ('template_char_block',)
    extra = 0

class FileBlockInline(admin.TabularInline):
    model = FileBlock
    exclude = ('template_block','filled',)
    raw_id_fields = ('template_file_block',)
    extra = 0

class ImageBlockInline(admin.TabularInline):
    model = ImageBlock
    exclude = ('template_block','filled',)
    raw_id_fields = ('template_image_block',)
    extra = 0

class AdBlockInline(admin.TabularInline):
    model = AdBlock
    exclude = ('template_block','filled',)
    raw_id_fields = ('template_ad_block',)
    extra = 0

class LayoutAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_filter = ('publication',)
    search_fields = ['publication__title']
    inlines = [
        CharBlockInline,
        FileBlockInline,
        ImageBlockInline,
        AdBlockInline,
        ]
        
class TemplateBlockAdmin(admin.ModelAdmin):
    list_filter = ('template',)
    search_fields = ['type__label']        

class AdLineInline(admin.TabularInline):
    model = AdLine
    extra = 1
    max_num = 12
    
class LineAdAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'publication', 'user', 'paid', 'setup_done')
    list_filter = ('paid', 'setup_done', 'publication')
    inlines = [
        AdLineInline,
    ]
    
class AdPriceLevelAdmin(admin.ModelAdmin):
    list_display = ('name','code','price')
  
class LeadAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('organization', 'contact_name', 'email', 'phone', 'publication')
    list_filter = ('publication',)
    search_fields = ['organization', 'contact_name', 'email', 'phone' 'publication__title']

class DisplayAdAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'publication', 'user', 'paid', 'setup_done')
    list_filter = ('paid', 'setup_done', 'publication')
            
class LeadStatusTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("description",)}

admin.site.register(PageCount, PageCountAdmin)
admin.site.register(SpreadType)
admin.site.register(SpreadTypeMap, SpreadTypeMapAdmin)
admin.site.register(BlockType)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(CoverTemplate, CoverTemplateAdmin)
admin.site.register(SpreadTemplate, SpreadTemplateAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(PublicationStatusType)
admin.site.register(Cover, LayoutAdmin)
admin.site.register(Spread, LayoutAdmin)
admin.site.register(TemplateCharBlock, TemplateBlockAdmin)
admin.site.register(TemplateFileBlock, TemplateBlockAdmin)
admin.site.register(TemplateImageBlock, TemplateBlockAdmin)
admin.site.register(TemplateAdBlock, TemplateBlockAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(File, FileImageAdmin)
admin.site.register(ImageCategory)
admin.site.register(LineAdCategory)
admin.site.register(AdSize)
admin.site.register(AdPriceLevel, AdPriceLevelAdmin)
admin.site.register(DisplayAd, DisplayAdAdmin)
admin.site.register(LineAd, LineAdAdmin)
admin.site.register(Lead, LeadAdmin)
admin.site.register(LeadStatusType, LeadStatusTypeAdmin)
