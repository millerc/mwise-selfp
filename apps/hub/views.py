from django.template import loader, Context
from django.http import Http404
from django.db.models import Q
from django.views.generic import list_detail
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from hub.models import *
from hub.forms import *
import datetime

def columnbrowser_places_by_state(request, slug):
    try:
        state = State.objects.get(slug=slug)
    except State.DoesNotExist:
        raise Http404

    return list_detail.object_list(
        request,
        queryset = Place.objects.filter(state=state,link__published=True).select_related('state').distinct().defer('geom','state__geom'),
        template_name = "hub/columnbrowser_places.html",
        template_object_name = "places",
        extra_context = {"state" : state}
    )

def places_by_state(request, slug):
    try:
        state = State.objects.get(slug=slug)
    except State.DoesNotExist:
        raise Http404

    return list_detail.object_list(
        request,
        queryset = Place.objects.filter(state=state,link__published=True).select_related('state').distinct().defer('geom','state__geom'),
        template_name = "hub/place_list.html",
        template_object_name = "places",
        extra_context = {"state" : state}
    )

def place_detail(request, place_slug):

    try:
        place = Place.objects.get(slug=place_slug)
        featured_links = Link.objects.filter(place=place,featured=True,published=True)
        nearby_places = Place.objects.all().distance(place.point).order_by('distance')
        #nearby_places = Place.objects.filter(link__published=True).distinct().distance(place.point).order_by('distance')
    except Place.DoesNotExist:
        raise Http404

    class weather:
        condition = 'Partly Cloudy with a Chance of Meatballs'
        temperature = 451
    
    if request.method == 'POST':
        link_form = LinkForm(request.POST)
        if link_form.is_valid():
            if "http://" in link_form.cleaned_data['description']:
                #do nothing and pretend like nothing is wrong
                abcde = 12345
            else:
	        cat = link_form.cleaned_data['category']
	        new_link = link_form.save()
	        listing = Listing(link=new_link,place=place,date_added=datetime.datetime.now())
	        listing.save()
	        catz = Categorization(link=new_link,category=cat)
	        catz.save()
	        t = loader.get_template('hub/link_new_email.txt')
	        c = Context({'link': new_link,'place': place,'category': cat, 'remote_addr':request.META['HTTP_X_FORWARDED_FOR'], })
	        #send_mail('Cloud Link Suggestion ', 'http://communitylink.com/admin/hub/link/' + str(new_link.id), 'cloud@communitylink.com', ['cloud@communitylink.com'], fail_silently=False)
	        send_mail('Cloud Link Suggestion ', t.render(c), 'cloud@communitylink.com', ['cloud@communitylink.com'], fail_silently=False)
            link_thanks = 'Thank you for suggesting this link. Once approved, it will appear in the listings.'
            link_form = LinkForm(
                initial={'url': 'http://'}
            )
            return render_to_response(
                'hub/place_detail.html', {
                    'link_thanks': link_thanks, 
                    'link_form': link_form, 
                    'nearby_places': nearby_places,
                    'place': place, 'state': place.state, 'featured_links': featured_links, 'weather': weather
                }
            )    
        else:
            return render_to_response('hub/place_detail.html', {'link_form': link_form, 'place': place, 'state': place.state, 'featured_links': featured_links, 'nearby_places': nearby_places})    
    else:
        link_form = LinkForm(
            initial={'url': 'http://'}
        )
        return render_to_response('hub/place_detail.html', {'link_form': link_form, 'place': place, 'state': place.state, 'featured_links': featured_links,'nearby_places': nearby_places})    

def place_links(request, place_slug):

    try:
        place = Place.objects.get(slug=place_slug)
        featured_links = Link.objects.filter(place=place,featured=True,published=True)
        nearby_places = Place.objects.all().distance(place.point).order_by('distance')
        #nearby_places = Place.objects.filter(link__published=True).distinct().distance(place.point).order_by('distance')
    except Place.DoesNotExist:
        raise Http404
        
    if request.method == 'POST':
        link_form = LinkForm(request.POST)
        if link_form.is_valid():
            cat = link_form.cleaned_data['category']
            new_link = link_form.save()
            listing = Listing(link=new_link,place=place,date_added=datetime.datetime.now())
            listing.save()
            catz = Categorization(link=new_link,category=cat)
            catz.save()
            send_mail('Cloud Link Suggestion ', 'http://communitylink.com/admin/hub/link/' + str(new_link.id), 'cloud@communitylink.com', ['cloud@communitylink.com'], fail_silently=False)
            link_thanks = 'Thank you for suggesting this link. Once approved, it will appear in the listings.'
            link_form = LinkForm(
                initial={'url': 'http://'}
            )
            return render_to_response(
                'hub/place_detail.html', {
                    'link_thanks': link_thanks, 
                    'link_form': link_form, 
                    'nearby_places': nearby_places,
                    'place': place, 'state': place.state, 'featured_links': featured_links
                }
            )    
        else:
            return render_to_response('hub/place_links.html', {'link_form': link_form, 'place': place, 'state': place.state, 'featured_links': featured_links, 'nearby_places': nearby_places})    
    else:
        link_form = LinkForm(
            initial={'url': 'http://'}
        )
        return render_to_response('hub/place_links.html', {'link_form': link_form, 'place': place, 'state': place.state, 'featured_links': featured_links,'nearby_places': nearby_places})    

def findplace(request):
    errors = []
    results = []
    query = ''
    state_list = State.objects.all()
    stusps = ''
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            errors.append('Enter a search term.')
        elif len(query) < 4:
            errors.append('Enter at least four characters.')
        else:
            stusps = request.GET['st']
            if stusps != '':
                results = Place.objects.filter(name__icontains=query,state__stusps=stusps)
            else:
                results = Place.objects.filter(name__icontains=query)
    return render_to_response("hub/find-community.html", {
    	"state_list": state_list,
    	"stusps": stusps,
    	"errors": errors,
        "results": results,
        "query": query  
    })

def hubstat(request):
    totalplaces = Place.objects.all().count()
    totalListings = Listing.objects.filter(link__published=True).count()
    listingsToday = Listing.objects.filter(link__published=True,date_added=datetime.datetime.today()).count()
    listingsSeven = Listing.objects.filter(link__published=True,date_added__gte=datetime.datetime.today()-datetime.timedelta(days=7)).count()
    listingsThirty = Listing.objects.filter(link__published=True,date_added__gte=datetime.datetime.today()-datetime.timedelta(days=30)).count()
    linkplaces = Place.objects.filter(link__published=True).distinct().defer('point','geom').count()
    linkplacesOne = Place.objects.filter(link__published=True,listing__date_added__lt=datetime.datetime.today()-datetime.timedelta(days=1)).distinct().defer('geom','point').count()
    linkplacesSeven = Place.objects.filter(link__published=True,listing__date_added__lt=datetime.datetime.today()-datetime.timedelta(days=7)).distinct().defer('geom','point').count()
    linkplacesThirty = Place.objects.filter(link__published=True,listing__date_added__lt=datetime.datetime.today()-datetime.timedelta(days=30)).distinct().defer('geom','point').count()
    featplaces = Place.objects.filter(link__featured=True,link__published=True).distinct().defer('point','geom').count()
    ufeatplaces = Place.objects.filter(Q(link__published=True),~Q(link__featured=True)).distinct().defer('point','geom').count()

    return render_to_response("hub/hub-stats.html", {
        "totalplaces": totalplaces,
        "totalListings": totalListings,
        "listingsToday": listingsToday,
        "listingsSeven": listingsSeven,
        "listingsThirty": listingsThirty,
        "linkplaces": linkplaces,
        "linkplacesOne": linkplacesOne,
        "linkplacesSeven": linkplacesSeven,
        "linkplacesThirty": linkplacesThirty,
        "featplaces": featplaces,
        "ufeatplaces": ufeatplaces
    })

