import simplejson
import urllib
import urllib2
from django.utils.encoding import smart_str
from django.contrib.gis.geos import Point

def get_lat(loc):
    location = urllib.quote_plus(smart_str(loc))
    dd = urllib2.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" % location).read() 
    ft = simplejson.loads(dd)
    if ft["status"] == 'OK':
       lat = ft["results"][0]['geometry']['location']['lat']
       lng = ft["results"][0]['geometry']['location']['lng']
       pnt = Point(lng, lat, srid=4326)
       return pnt
 
