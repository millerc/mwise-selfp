from hub.models import *
from django.db import transaction

@transaction.autocommit
def run(verbose=True):

    pls = Place.objects.filter(zip_codes__isnull=True).defer("geom").iterator()
    for pl in pls:
        try:
            zps = ZipCode.objects.filter(geom__intersects=pl.geom.boundary).iterator()
            for zp in zps:
                pl.zip_codes.add(zp)
                pl.save()
                print pl, " ", zp
        except:
            transaction.rollback()
            print "Error: ", pl