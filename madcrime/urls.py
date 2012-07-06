from django.conf.urls.defaults import *
from madcrime.views import index, detail

urlpatterns = patterns('',
    url(
        regex   = r'^$',
        view    = index,
        kwargs  = {},
        name    = 'incident-table',
    ),

    url(
        regex   = r'^(?P<incident_id>\d+)/$',
        view    = detail,
        kwargs  = {},
        name    = 'details-table',
    ),

    url(r'^search/', include('haystack.urls')),

)