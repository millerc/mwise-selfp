import os
from django.contrib.gis.utils import LayerMapping
from models import County

county_mapping = {
    'statefp' : 'STATEFP',
    'countyfp' : 'COUNTYFP',
    'countyns' : 'COUNTYNS',
    'cntyidfp' : 'CNTYIDFP',
    'name' : 'NAME',
    'namelsad' : 'NAMELSAD',
    'lsad' : 'LSAD',
    'classfp' : 'CLASSFP',
    'mtfcc' : 'MTFCC',
    'csafp' : 'CSAFP',
    'cbsafp' : 'CBSAFP',
    'metdivfp' : 'METDIVFP',
    'funcstat' : 'FUNCSTAT',
    'geom' : 'MULTIPOLYGON',
}

county_shp = '/home/cmiller/django/chub/hub/shp/tl_2009_us_county.shp'

def run(verbose=True):
    lm = LayerMapping(County, county_shp, county_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)
