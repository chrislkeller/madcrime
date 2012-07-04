#MadCrime:#
##A round-up of Madison Police Department Incident Reports##

###About###
----
A working title, [MadCrime's](http://madcrime.chrislkeller.com/) basic functionality uses Python to scrape a [table](http://www.cityofmadison.com/incidentReports/incidentlist.cfm?a=71) of [Madison Police Department](http://www.cityofmadison.com/police/) incident reports and display the content to the user.

From the [list of reports](http://madcrime.chrislkeller.com/incidents/), a user can click through to see the location of the incident and read the details. To the best of my ability I tried to format the details to resemble sentences, but much of that is above my skill level at this point.

###Install & Run The Scraper###
----
- Download the zip file or fork the repo. Cd to your project directory and run pip install -r requirements.txt. I've been using the following for madcrime:

	BeautifulSoup==3.2.1
	
	Django==1.4
	
	South==0.7.5
	
	geopy==0.94.2
	
	mechanize==0.2.5
	
	mimeparse==0.1.3
	
	python-dateutil==1.5
	
	virtualenv==1.7.1.2
	
	virtualenv-clone==0.2.4
	
	virtualenvwrapper==3.5
	
	wsgiref==0.1.2
	
	yolk==0.4.3

- Add 'madcrime' to INSTALLED_APPS in settings.py.

- Add (r'^incidents/', include('madcrime.urls')) to urls.py

- Run python manage.py syncdb from your project directory.

- To scrape run python manage.py scrapepd from your project directory.

- Run python manage.py runserver and navigate to /incidents, and hopefully you see a list of incidents.

- The scraper is located in madcrime/management/commands/scrapepd.py

###Ideas to take this further###
----
####User Improvements####
- Search, search, search: Plain text, by date, by incident type, by address or radius.
- Add a method of narrowing incidents on the main map by similar search criteria.
- Determine if content from Madison's Most Wanted and CrimeStoppers has a place.
- Determine how to handle cases that aren't posted.
- <del>Add map to main page with markers locating where incidents occured.</del>
- Add map with aldermanic ward polygons.
- Alert system for when new incidents are loaded.
- Hook in with Wis Circuit Court Access queries?
- Table view should appear in descending order.
- Sorting of Incidents using tablesorter or datatables jQuery plugins.
- Add layers of demographic data or other interesting tidbits.
- Query madison.com and other local news sources for information about the incidents.

####Admin Improvements####
- Rich text editor.
- Ponder addition of a queue manager that holds incident details until they are edited/reviewed.
- Sort incidents by release date in admin .
- Templates Improvements

####MVC Improvements####
- <del>Find new method of geocoding addresses and storing them so Incidents model can access this information.</del>
- Rename model information, or make json output dev friendly.

####Scraper Improvements####
- <del>Add command line input, asking user which page to scrape</del>.
- Cron job to run the scraper twice daily.
- Learn RegExpressions and python methods to split Date and Time -- stored in incidentDetails -- into separate values.
- Learn RegExpressions and python methods to split suspect/arrest information -- stored in suspectDetails and arrestDetails -- into separate values.

###License###
----
The MIT License