# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from django.contrib.gis.geos import Point

from hub.models import Place
from accesspoint.models import POI

@csrf_exempt
def nearby_communities(request):
    if request.method == 'POST':
        lon = float(request.POST['lon'])
        lat = float(request.POST['lat'])
        point = Point(lon, lat, srid=4326)
        nearby_places = Place.objects.all().distance(point).order_by('distance')
    
        return render_to_response("accesspoint/nearby_communities.json", {
            "places": nearby_places[:20],
        }, context_instance=RequestContext(request))
    
    else:
        point = Point(-90, 45, srid=4326)
        nearby_places = Place.objects.all().distance(point).order_by('distance')

        return render_to_response("accesspoint/nearby_communities.json", {
            "places": nearby_places[:20],
        }, context_instance=RequestContext(request))

@csrf_exempt
def nearby_points(request):
    if request.method == 'POST':
        lon = float(request.POST['lon'])
        lat = float(request.POST['lat'])
        point = Point(lon, lat, srid=4326)
        nearby_places = POI.objects.all().distance(point).order_by('distance')
    
        return render_to_response("accesspoint/nearby_communities.json", {
            "places": nearby_places[:30],
        }, context_instance=RequestContext(request))
    
    else:
        point = Point(-89.668195, 39.776031, srid=4326)
        nearby_places = POI.objects.all().distance(point).order_by('distance')

        return render_to_response("accesspoint/nearby_communities.json", {
            "places": nearby_places[:30],
        }, context_instance=RequestContext(request))
