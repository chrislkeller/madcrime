# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core import serializers
from django.template import RequestContext
from madcrime.models import Incident
from easy_maps.models import Address

#the main index request
def index(request):

    #tells how the output should be structured
    incident_listing = Incident.objects.all().order_by('-dateDetails', 'typeDetails')

    #returns an HttpResponse object of the given template
    return render_to_response('incident-table.html', {'incident_listing': incident_listing})

#details request
def detail(request, incident_id):

    p = get_object_or_404(Incident, pk=incident_id)
    return render_to_response('details-table.html', {'incident': p},
        context_instance=RequestContext(request))
        
#the main index request
#def index(request):

    #tells how the output should be structured
    #addresses = Address.objects.filter(geocode_error=False)

    #returns an HttpResponse object of the given template
    #return render_to_response('incident-map.html', {'addresses': addresses},
        #context_instance=RequestContext(request))