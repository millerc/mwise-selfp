from django.conf.urls.defaults import *
from accesspoint.views import nearby_communities, nearby_points

urlpatterns = patterns('',
    url(r"^nearby-communities/", nearby_communities),
    url(r"^nearby-points/", nearby_points),
)
