import os
import glob
from django.contrib.gis.utils import LayerMapping
from models import ZipCode

zipcode_mapping = {
    'zcta5ce' : 'ZCTA5CE',
    'classfp' : 'CLASSFP',
    'mtfcc' : 'MTFCC',
    'funcstat' : 'FUNCSTAT',
    'aland' : 'ALAND',
    'awater' : 'AWATER',
    'intptlat' : 'INTPTLAT',
    'intptlon' : 'INTPTLON',
    'geom' : 'MULTIPOLYGON',
}

#zcta5_shp = '/home/cmiller/django/chub/hub/shp/tl_2009_17_zcta5.shp'

path = glob.glob('/home/cmiller/django/chub/hub/shp/*zcta5.shp')

def run(verbose=True):
    for zcta5_shp in path:
        try:
            print 'Processing: ' + zcta5_shp
            lm = LayerMapping(ZipCode, zcta5_shp, zipcode_mapping,
                          transform=False, encoding='iso-8859-1')
       
            lm.save(strict=True, verbose=verbose)
        except:
            print 'Error: ' + zcta5_shp
