from madcrime.models import Incident
from django.contrib import admin

class IncidentAdmin(admin.ModelAdmin):

	list_display = ('dateDetails', 'dateIncidents', 'typeDetails', 'addressDetails', 'computed_address', 'geocode_error', 'suspectDetails', 'arrestedDetails', 'victimDetails')

    	fieldsets = [
    	   ('Release Date', {'fields': ['dateIncidents']}),
    	   ('Incident Date', {'fields': ['dateDetails']}),
    	   ('Incident Type', {'fields': ['typeDetails']}),
    	   ('Incident Link', {'fields': ['linkIncidents']}),
    	   ('Incident Address', {'fields': ['addressDetails']}),
    	   ('Computed Address', {'fields': ['computed_address']}),
    	   ('Lat', {'fields': ['latitude']}),
    	   ('Long', {'fields': ['longitude']}),
    	   ('Error', {'fields': ['geocode_error']}),
    	   ('Incident Case', {'fields': ['caseIncidents']}),
    	   ('Incident Suspects', {'fields': ['suspectDetails']}),
    	   ('Incident Arrested', {'fields': ['arrestedDetails']}),
    	   ('Incident Victim', {'fields': ['victimDetails']}),
    	   ('Incident Details', {'fields': ['detailsDetails']}),
		]

	list_filter = ['geocode_error', 'dateDetails', 'typeDetails']
	search_fields = ['dateIncidents', 'dateDetails', 'typeDetails', 'linkIncidents', 'addressDetails', 'caseIncidents', 'suspectDetails', 'arrestedDetails', 'victimDetails', 'detailsDetails']

admin.site.register(Incident, IncidentAdmin)