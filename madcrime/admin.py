from madcrime.models import Incident
from django.contrib import admin

class IncidentAdmin(admin.ModelAdmin):

	list_display = ('dateDetails', 'dateIncidents', 'typeDetails', 'addressDetails', 'suspectDetails', 'arrestedDetails', 'victimDetails')

    	fieldsets = [
    	   ('Release Date', {'fields': ['dateIncidents']}),
    	   ('Incident Date', {'fields': ['dateDetails']}),
    	   ('Incident Type', {'fields': ['typeDetails']}),
    	   ('Incident Link', {'fields': ['linkIncidents']}),
    	   ('Incident Address', {'fields': ['addressDetails']}),
    	   ('Incident Case', {'fields': ['caseIncidents']}),
    	   ('Incident Suspects', {'fields': ['suspectDetails']}),
    	   ('Incident Arrested', {'fields': ['arrestedDetails']}),
    	   ('Incident Victim', {'fields': ['victimDetails']}),
    	   ('Incident Details', {'fields': ['detailsDetails']}),
		]

	list_filter = ['dateDetails', 'typeDetails']
	search_fields = ['dateIncidents', 'dateDetails', 'typeDetails', 'linkIncidents', 'addressDetails', 'caseIncidents', 'suspectDetails', 'arrestedDetails', 'victimDetails', 'detailsDetails']

admin.site.register(Incident, IncidentAdmin)