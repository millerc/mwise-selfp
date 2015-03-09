from hub.models import *
from django.db import transaction

@transaction.autocommit
def run(verbose=True):

    pls = Place.objects.filter(counties__isnull=True).defer("geom").iterator()
    for pl in pls:
        cos_st = County.objects.filter(statefp=pl.statefp)
        try:
            coc = cos_st.filter(geom__contains=pl.geom.centroid)
            for co in coc:
                pl.counties.add(co)
                pl.save()
                print pl, " ", co
        except:
            transaction.rollback()
            print "Error: ", pl