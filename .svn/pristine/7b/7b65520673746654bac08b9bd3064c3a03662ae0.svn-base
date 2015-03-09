import os
import glob
from django.contrib.gis.utils import LayerMapping
from models import Place

place_mapping = {
    'statefp' : 'STATEFP',
    'placefp' : 'PLACEFP',
    'placens' : 'PLACENS',
    'plcidfp' : 'PLCIDFP',
    'name' : 'NAME',
    'namelsad' : 'NAMELSAD',
    'lsad' : 'LSAD',
    'classfp' : 'CLASSFP',
    'cpi' : 'CPI',
    'pcicbsa' : 'PCICBSA',
    'pcinecta' : 'PCINECTA',
    'mtfcc' : 'MTFCC',
    'funcstat' : 'FUNCSTAT',
    'geom' : 'MULTIPOLYGON',
}

#place_shp = '/home/cmiller/django/chub/hub/shp/tl_2009_19_place.shp'

path = glob.glob('/home/cmiller/django/chub/hub/shp/*place.shp')

def run(verbose=True):
    for place_shp in path:
        lm = LayerMapping(Place, place_shp, place_mapping,
                      transform=False, encoding='iso-8859-1')

        lm.save(strict=True, verbose=verbose)