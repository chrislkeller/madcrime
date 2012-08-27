import urllib
import urllib2
import re
import types
import time, datetime
from django.core.management.base import BaseCommand
from madcrime.models import Incident
from mechanize import Browser
from BeautifulSoup import BeautifulSoup, Tag
from django.utils.encoding import smart_str, smart_unicode
from dateutil import parser

class Command(BaseCommand):
    help = 'Scrapes Madison Police Department Data\nScraper takes input for a beginning page number and an ending page number, and the scraper uses Beautiful Soup to scrape the details and write them to a django model.'

    def handle(self, *args, **options):
        pageNumber = raw_input('What is the first page you would like to scrape?')
        endNumber = raw_input('What is the last page you would like to scrape?')
        countLoop = int(pageNumber)
        endLoop = int(endNumber)

        print ('\nStarting scrape at %s\n' % (datetime.datetime.now()))

        while (countLoop <= endLoop):

            # set some varibles to make life easier
            prefixIncidents = 'http://www.cityofmadison.com/incidentReports/'
            countIncidents = 0
            addressSuffix = ', Madison, Wis.'

            # use selectors to whittle
            # down to the content
            mech = Browser()
            urlIncidents = 'http://www.cityofmadison.com/incidentReports/incidentList.cfm?a=71&page=' + str(countLoop)
            pageIncidents = mech.open(urlIncidents)
            htmlIncidents = pageIncidents.read()
            soupIncidents = BeautifulSoup(htmlIncidents, convertEntities=BeautifulSoup.HTML_ENTITIES)
            tableIncidents = soupIncidents.find('table', {'id': 'list'})
            rowsIncidents = tableIncidents.findAll('tr')[1:]

            # get length for our loop
            lengthIncidents = len(rowsIncidents)

            for row in rowsIncidents:

                # whittle through content
                cells = row.findAll('td')
                dateIncidents = cells[0].string

                # use dateutil to convert string to date/time object
                convertedDateIncidents = parser.parse(dateIncidents)
                linkIncidents = prefixIncidents + cells[1].a['href']
                caseIncidents  = cells[2].text.encode('utf-8')

                # save content to django models
                try:
                    obj = Incident.objects.get(caseIncidents = caseIncidents)
                    obj.dateIncidents = convertedDateIncidents
                    obj.linkIncidents = linkIncidents
                    obj.caseIncidents = caseIncidents
                    obj.save()
                except Incident.DoesNotExist:
                    obj = Incident(dateIncidents = convertedDateIncidents, linkIncidents=linkIncidents, caseIncidents = caseIncidents)
                    obj.save()

                    # down to the content
                    # use selectors to whittle
                    mech = Browser()
                    urlDetails = linkIncidents
                    pageDetails = mech.open(urlDetails)
                    htmlDetails = pageDetails.read()
                    soupDetails = BeautifulSoup(htmlDetails, convertEntities=BeautifulSoup.HTML_ENTITIES)

                    # replaces br tags with periods
                    for breakPoint in soupDetails.findAll('br'):
                        new = "."
                        breakPoint.replaceWith(new)

                    # hits incident detail table and returns the contents
                    tableDetails = soupDetails.find('table', {'id': 'incidentdetail'})

                    # finds the tbody that contains the data
                    bodyDetails = tableDetails.find('tbody')

                    # find all of the rows in the table
                    rowsDetails = bodyDetails.findAll('tr')

                    # create an empty dict
                    models = {}

                    # determine how many rows in the table
                    lengthDetails = len(rowsDetails)

                    # set the count
                    countDetails = 0

                    # each row do this
                    while (countDetails < lengthDetails):
                        for item in rowsDetails:
                            # create pairs
                            labelDetails = item.find('th').text
                            dataDetails = item.find('td').text

                            # add to dict
                            models[labelDetails] = dataDetails

                            # repeat loop
                            countDetails = countDetails + 1

                            #print models
                            if models.has_key('Incident Date'):
                                dateDetails = models['Incident Date']
                                convertedDateDetails = parser.parse(dateDetails)

                            if models.has_key('Incident Type'):
                                typeDetails = models['Incident Type']

                            if models.has_key('Address'):
                                addressDetails = models['Address']
                                addressDetails = addressDetails + addressSuffix

                            if models.has_key('Suspect(s)'):
                                suspectDetails = models['Suspect(s)']
                            else:
                                suspectDetails = 'None'

                            # adds space after period
                            p = re.compile('(\S)\.(\S)')
                            suspectOutput = re.sub(p, '\g<1>. \g<2>', suspectDetails)

                            if models.has_key('Arrested'):
                                arrestedDetails = models['Arrested']
                            else:
                                arrestedDetails = 'None'

                            # adds space after period
                            p = re.compile('(\S)\.(\S)')
                            arrestOutput = re.sub(p, '\g<1>. \g<2>', arrestedDetails)

                            if models.has_key('Victim'):
                                victimDetails = models['Victim']
                            else:
                                victimDetails = 'None'

                            if models.has_key('Details'):
                                detailsDetails = models['Details']

                                try:
                                    obj = Incident.objects.get(linkIncidents = linkIncidents)
                                    obj.dateDetails = convertedDateDetails
                                    obj.dateIncidents = convertedDateIncidents
                                    obj.typeDetails = typeDetails
                                    obj.addressDetails = addressDetails
                                    obj.suspectDetails = suspectDetails
                                    obj.arrestedDetails = arrestedDetails
                                    obj.victimDetails = victimDetails
                                    obj.detailsDetails = detailsDetails[:3000]
                                    obj.caseIncidents = caseIncidents
                                    obj.save()
                                except Incident.DoesNotExist:
                                    obj = Incident(dateDetails = convertedDateDetails, dateIncidents = convertedDateIncidents, typeDetails = typeDetails, addressDetails = addressDetails, suspectDetails = suspectDetails, arrestedDetails = arrestedDetails, victimDetails = victimDetails, detailsDetails = detailsDetails[:3000], caseIncidents = caseIncidents)
                                    obj.save()

            print ('Finished scraping %s\n' % (urlIncidents))
            countLoop = countLoop + 1

        print ('\nScrape finished at %s\n' % str(datetime.datetime.now()))