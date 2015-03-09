from django.contrib import admin

from marketwise.models import Template, TemplateCharBlock, TemplateTextBlock, TemplateImageBlock, TemplateClassificationIndustry, TemplateClassificationPurpose, TemplateClassificationFormat, TemplateClassificationColor, TemplateTypeIndustry, TemplateTypePurpose, TemplateTypeFormat, TemplateTypeColor, Customization, CharBlock, TextBlock, ImageBlock, CustomizationStatusType

class TemplateCharBlockInline(admin.StackedInline):
    model = TemplateCharBlock
    extra = 0

class TemplateTextBlockInline(admin.StackedInline):
    model = TemplateTextBlock
    extra = 0

class TemplateImageBlockInline(admin.StackedInline):
    model = TemplateImageBlock
    extra = 0
    
class TemplateClassificationIndustryInline(admin.TabularInline):
    model = TemplateClassificationIndustry
    extra = 0

class TemplateClassificationPurposeInline(admin.TabularInline):
    model = TemplateClassificationPurpose
    extra = 0

class TemplateClassificationFormatInline(admin.TabularInline):
    model = TemplateClassificationFormat
    extra = 0

class TemplateClassificationColorInline(admin.TabularInline):
    model = TemplateClassificationColor
    extra = 0
    
class TemplateAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ('name', 'slug', 'description', 'keywords', 'rank')
    list_editable = ('keywords', 'rank')
    list_filter = ('credits_required',)
    search_fields = ['name']
    filter_horizontal = ('color_variations','related_templates','suggested_templates',)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        TemplateCharBlockInline,
        TemplateTextBlockInline,
        TemplateImageBlockInline,
        TemplateClassificationIndustryInline,
        TemplateClassificationPurposeInline,
        TemplateClassificationFormatInline,
        TemplateClassificationColorInline,
        ]
        
class TemplateTypeAdmin(admin.ModelAdmin):
    list_display = ('description', 'slug', 'parent_type')
    prepopulated_fields = {"slug": ("description",)}

class CharBlockInline(admin.StackedInline):
    model = CharBlock
    extra = 0

class TextBlockInline(admin.StackedInline):
    model = TextBlock
    extra = 0

class ImageBlockInline(admin.StackedInline):
    model = ImageBlock
    extra = 0

class CustomizationAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('template', 'user', 'status', 'added', 'updated')
    list_filter = ('status', 'added', 'updated')
    search_fields = ['template', 'user',]
    inlines = [
        CharBlockInline,
        TextBlockInline,
        ImageBlockInline,
        ]

class CustomizationStatusTypeAdmin(admin.ModelAdmin):
    list_display = ('description', 'slug')
    prepopulated_fields = {"slug": ("description",)}

#class TemplateTypePurposeAdmin(admin.ModelAdmin):
#    filter_horizontal = ('industries',)
    
#class TemplateClassificationPurposeAdmin(admin.ModelAdmin):
#    def formfield_for_foreignkey(self, db_field, request, **kwargs):
#        if db_field.name == "car":
#            kwargs["queryset"] = Car.objects.filter(owner=request.user)
#            return db_field.formfield(**kwargs)
#        return super(MyModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

        
admin.site.register(Template, TemplateAdmin)
admin.site.register(Customization, CustomizationAdmin)
#admin.site.register(BlockType)

admin.site.register(TemplateTypeIndustry, TemplateTypeAdmin)
admin.site.register(TemplateTypePurpose, TemplateTypeAdmin)
admin.site.register(TemplateTypeFormat, TemplateTypeAdmin)
admin.site.register(TemplateTypeColor, TemplateTypeAdmin)

admin.site.register(CustomizationStatusType, CustomizationStatusTypeAdmin)