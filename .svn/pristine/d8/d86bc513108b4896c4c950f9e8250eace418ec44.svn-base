# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from django.contrib.auth.decorators import login_required

from selfpublish.models import Publication, LineAd, DisplayAd, Ad

@login_required
def dashboard_home(request):
    publications = Publication.objects.filter(owner=request.user)
    line_ads = LineAd.objects.filter(user=request.user)
    display_ads = DisplayAd.objects.filter(user=request.user)
    return render_to_response("dashboard/home.html", {
        "publications": publications,
        "line_ads": line_ads,
        "display_ads": display_ads,
    }, context_instance=RequestContext(request))
    
@login_required
def dashboard_otb(request):
    publications = Publication.objects.filter(owner=request.user)
    return render_to_response("dashboard/otb.html", {
        "publications": publications,
    }, context_instance=RequestContext(request))
