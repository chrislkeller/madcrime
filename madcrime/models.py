from django.conf import settings
from django.db import models
from django.utils.encoding import smart_str
from geopy import geocoders
import datetime

# Create your models here.
class Incident(models.Model):
    dateIncidents = models.DateField(null=True, blank=True)
    dateDetails = models.DateTimeField(null=True, blank=True)
    typeDetails = models.CharField(max_length=1024)
    linkIncidents = models.CharField(max_length=1024)
    addressDetails = models.CharField(max_length=255, db_index=True)
    computed_address = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    geocode_error = models.BooleanField(default=False)
    caseIncidents = models.CharField(max_length=1024)
    suspectDetails = models.TextField(blank=True, null=True)
    arrestedDetails = models.TextField(blank=True, null=True)
    victimDetails = models.TextField(blank=True, null=True)
    detailsDetails = models.TextField()

    class Meta:
        ordering = ["-dateDetails"]

    # this taken from easy_maps base code for geocoding
    def fill_geocode_data(self):
        if not self.addressDetails:
            self.geocode_error = True
            return
        try:
            if hasattr(settings, "EASY_MAPS_GOOGLE_KEY") and settings.EASY_MAPS_GOOGLE_KEY:
                g = geocoders.Google(settings.EASY_MAPS_GOOGLE_KEY)
            else:
                g = geocoders.Google(resource='maps')
            address = smart_str(self.addressDetails)
            self.computed_address, (self.latitude, self.longitude,) = g.geocode(address)
            self.geocode_error = False
        except (UnboundLocalError, ValueError,geocoders.google.GQueryError):
            self.geocode_error = True

    def save(self, *args, **kwargs):
        # fill geocode data if it is unknown
        if (self.longitude is None) or (self.latitude is None):
            self.fill_geocode_data()
        super(Incident, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.addressDetails