from django.contrib import admin
from django.contrib.gis import admin
from django.contrib.gis.maps.google import GoogleMap
from models import *

GMAP = GoogleMap(key='ABQIAAAAc061ocUXMFvfLalN3YaLyhQxyVlcfyA1pASQj_k0LU3TMdaxIhSSHzVmVu-ccw0f37W4hwGDtGKoIg')

class GoogleAdmin(admin.OSMGeoAdmin):
    extra_js = [GMAP.api_url + GMAP.key]
    map_template = 'gis/admin/google.html'
    default_lon = -10965893.794911034
    default_lat = 4841747.3774259118
    map_width = 768
    map_height = 512

class PlacesInline(admin.TabularInline):
    model = Chamber.places.through
    extra = 1
    raw_id_fields = ('place',)

class POIAdmin(GoogleAdmin):
    search_fields = ('name','description')
    list_display = ('name','address','address_line_2','city','state','url','email','phone')
    list_filter = ('state','city' )
    fieldsets = (
        (None, {
            'fields': ('published', 'name', 'description', 'address', 'city', 'state', 'zip', 'phone', 'email', 'url','categories')
        }),
        ('Map', {
            'classes': ('collapse',),
            'fields': ('point',)
        }),
        )

class ChamberAdmin(POIAdmin):
    inlines = [ PlacesInline, ]
    
class MemberAdmin(POIAdmin):
    filter_horizontal = ('categories',)

admin.site.register(Chamber, ChamberAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(POI, POIAdmin)
admin.site.register(Category)