from django.db import models
import datetime

# Create your models here.
class Incident(models.Model):
    dateIncidents = models.CharField(max_length=1024)
    dateDetails = models.CharField(max_length=1024)
    typeDetails = models.CharField(max_length=1024)
    linkIncidents = models.CharField(max_length=1024)
    addressDetails = models.CharField(max_length=1024)
    caseIncidents = models.CharField(max_length=1024)
    suspectDetails = models.TextField(blank=True, null=True)
    arrestedDetails = models.TextField(blank=True, null=True)
    victimDetails = models.TextField(blank=True, null=True)
    detailsDetails = models.TextField()
    def __unicode__(self):
        return self.caseIncidents
    
    def sorted_patients(self):
        return u"%s" % (self.addressDetails)