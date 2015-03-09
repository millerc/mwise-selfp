from django.contrib import admin
from django.contrib.gis import admin
from django.contrib.gis.maps.google import GoogleMap
from models import *

GMAP = GoogleMap(key='ABQIAAAAc061ocUXMFvfLalN3YaLyhQxyVlcfyA1pASQj_k0LU3TMdaxIhSSHzVmVu-ccw0f37W4hwGDtGKoIg')

class GoogleAdmin(admin.OSMGeoAdmin):
    extra_js = [GMAP.api_url + GMAP.key]
    map_template = 'gis/admin/google.html'

class PlaceCountyInline(admin.TabularInline):
     model = Place.counties.through
     extra = 1
     raw_id_fields = ('place','county',)

class PlaceZipCodesInline(admin.TabularInline):
     model = Place.zip_codes.through
     extra = 2
     raw_id_fields = ('place','zipcode',)

class LinkPlaceInline(admin.TabularInline):
     model = Link.place.through
     raw_id_fields = ('link','place',)

class ListingInline(admin.TabularInline):
    model = Listing
    extra = 2
    raw_id_fields = ('place',)

class CategorizationInline(admin.TabularInline):
    model = Categorization
    extra = 3
    raw_id_fields = ('link',)
    
class StateAdmin(GoogleAdmin):
     list_display = ('name','stusps')
     search_fields = ('name',)
#     prepopulated_fields = {'slug': ('name',)}

     fieldsets = (
       ('State Attributes', {'fields': (('name','stusps','slug',))}),
       ('Map View', {'fields': ('geom',)}),
     )

     # Default GeoDjango OpenLayers map options
     scrollable = False
     map_width = 700
     map_height = 325
     default_lon = -89
     default_lat = 40

class CountyAdmin(GoogleAdmin):
     inlines = [ PlaceCountyInline, ]
     list_display = ('namelsad','state',)
     list_filter = ('state',)
     search_fields = ('name',)

     fieldsets = (
       ('County Attributes', {'fields': (('name','slug','state','namelsad',))}),
       ('Map View', {'fields': ('geom',)}),
     )

     # Default GeoDjango OpenLayers map options
     scrollable = False
     map_width = 700
     map_height = 325
     default_lon = -89
     default_lat = 40
     
class PlaceAdmin(GoogleAdmin):
     inlines = [ LinkPlaceInline, PlaceCountyInline, PlaceZipCodesInline ]
     list_display = ('name','state','county_list','elevation','current_population','primary_zip_code')
     list_filter = ('state',)
     search_fields = ('name',)
     raw_id_fields = ('counties',)
     
     fieldsets = (
       ('Place Attributes', {'fields': 	(('name','slug','state','elevation','current_population','primary_zip_code','twitter_query'))}),
       ('Map View', {'fields': ('geom','point')}),
     )

     # Default GeoDjango OpenLayers map options
     scrollable = False
     map_width = 700
     map_height = 325
     default_lon = -89
     default_lat = 40

class ZipCodeAdmin(GoogleAdmin):
     list_display = ('zcta5ce',)
     search_fields = ('zcta5ce',)
     fieldsets = (
       ('Zip Code Attributes', {'fields': (('zcta5ce','intptlat','intptlon',))}),
       ('Map View', {'fields': ('geom',)}),
     )

     # Default GeoDjango OpenLayers map options
     scrollable = False
     map_width = 700
     map_height = 325
     default_lon = -89
     default_lat = 40     

class LinkAdmin(admin.ModelAdmin):
     filter_horizontal = ('categories', )
     inlines = [ListingInline, CategorizationInline]
     list_display = ('name','place_list','url','published','featured','category_list',)
     search_fields = ('name',)
     list_filter = ('published','featured')
     fieldsets = (
       ('Link Attributes', {
       	   'fields': ('name','url','description')
       }),
       ('Link Settings', {
       	   'fields': ('published','featured')
       }),
     )
     
class ListingAdmin(admin.ModelAdmin):
     raw_id_fields = ('place','link',)
     search_fields = ('date_added',)

class CategoryAdmin(admin.ModelAdmin):
     list_display = ('name','description',)
     search_fields = ('name','description',)
     
admin.site.register(State, StateAdmin)
admin.site.register(County, CountyAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(ZipCode, ZipCodeAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Listing, ListingAdmin)
