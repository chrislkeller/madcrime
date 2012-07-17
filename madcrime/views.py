# Create your views here
from datetime import datetime, date, time, timedelta
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core import serializers
from django.template import RequestContext
from madcrime.models import Incident

# the main index request
# filter incidents from the last week
def index(request):
   startdate = date.today()
   enddate = timedelta(days=7)
   displaydate = startdate - enddate
   incident_listing = Incident.objects.filter(dateDetails__gte=displaydate)
   return render_to_response('incident-table.html', {'incident_listing': incident_listing})
        
# details request
def detail(request, incident_id):
    p = get_object_or_404(Incident, pk=incident_id)
    return render_to_response('details-table.html', {'incident': p},
        context_instance=RequestContext(request))