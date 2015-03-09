import os
from django.contrib.gis.utils import LayerMapping
from models import State

state_mapping = {
    'region' : 'REGION',
    'division' : 'DIVISION',
    'statefp' : 'STATEFP',
    'statens' : 'STATENS',
    'stusps' : 'STUSPS',
    'name' : 'NAME',
    'lsad' : 'LSAD',
    'mtfcc' : 'MTFCC',
    'funcstat' : 'FUNCSTAT',
    'aland' : 'ALAND',
    'awater' : 'AWATER',
    'intptlat' : 'INTPTLAT',
    'intptlon' : 'INTPTLON',
    'geom' : 'MULTIPOLYGON',
}

state_shp = '/home/cmiller/django/chub/hub/shp/tl_2009_us_state.shp'

def run(verbose=True):
    lm = LayerMapping(State, state_shp, state_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)
