# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf.urls.static import static
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.contrib import admin
admin.autodiscover()

from hub.models import *
from hub.views import *

# Move to HUB app
columnbrowser_states = {
    'queryset': Place.objects.filter(link__published=True).select_related('state').distinct().order_by('state').defer('geom','state__geom'),
    'template_name': 'hub/columnbrowser_states.html',
}
recent_activity_balloons = {
    'queryset': Listing.objects.exclude(place__state__id=1).exclude(place__state__id=5).exclude(place__state__id=19).exclude(place__state__id=7).exclude(place__state__id=27).exclude(place__state__id=38).exclude(place__state__id=28).select_related('link','place','place__state').defer(),
    'template_name': 'hub/recent_activity_balloons.html',
}

from pinax.apps.account.openid_consumer import PinaxConsumer

handler500 = "pinax.views.server_error"

#from projects.models import MediaKit
#from orders.views import purchase

#mediakit_detail_info = {
#    "queryset": MediaKit.objects.all(),
#    "slug_field": 'publication__slug',
#}

urlpatterns = patterns("",
    url(r"^$", direct_to_template, {
        "template": "homepage.html",
    }, name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^admin/invite_user/$", "pinax.apps.signup_codes.views.admin_invite_user", name="admin_invite_user"),
    url(r"^about/", include("about.urls")),
    url(r"^account/", include("pinax.apps.account.urls")),
    url(r"^openid/(.*)", PinaxConsumer()),
    url(r"^profiles/", include("idios.urls")),
    url(r"^notices/", include("notification.urls")),
    url(r"^announcements/", include("announcements.urls")),

    url(r"^dashboard/", include("dashboard.urls")),
    url(r"^accesspoint/", include("accesspoint.urls")),
    url(r"^marketwise/", include("marketwise.urls")),
    url(r"^qbms/", include("qbms.urls")),
    url(r"^self-publish/", include("selfpublish.urls")),
    
    #url(r'^projects/', include('projects.urls')),
    #url(r'^orders/', include('orders.urls')),
    #
    #url(r'^media-kits/(?P<slug>[-\w]+)/$', list_detail.object_detail, mediakit_detail_info, name="mediakit_detail"),
    #url(r'^purchase/(?P<key>[-\w]+)/$', 'orders.views.purchase', name="purchase_detail"),

    
    url(r"^import/", include('csvimporter.urls')),

    # Hub FIXME!
    url(r"^columnbrowser/states/([-\w]+)/$", columnbrowser_places_by_state, name="cb_places"),
    url(r"^columnbrowser/states/$", 'django.views.generic.list_detail.object_list', columnbrowser_states, name="cb_states"),
    url(r"^state/([-\w]+)/$", places_by_state, name="state"),
    url(r"^recent-activity-balloons/$", 'django.views.generic.list_detail.object_list', recent_activity_balloons, name="cloud_recent"),
    url(r"^find-community/$", 'findplace', name="find_place"),
    url(r"^suggest-link/$", 'findplace', name="suggest_link"),
    url(r"^hub-stats/$", 'hubstat', name="hubstat"),
    url(r"^api/links/([-\w]+)/$", place_links, name="api_place_links"),
    url(r"^([-\w]+)/$", place_detail),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)