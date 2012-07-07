#MadCrime:#
##A round-up of Madison Police Department Incident Reports##

###About###
----
MadCrime is the Django app -- or rather Python scraper -- behind [MadSafety](http://www.madsafety.nwsmkr.com/incidents), which is a table of [Madison Police Department](http://www.cityofmadison.com/police/) incident [reports](http://www.cityofmadison.com/incidentReports/incidentlist.cfm?a=71).

From the list of reports, a user can click through to see the location of the incident and read the details.

I hope to have MadFire -- a Python scraper for incident reports from the Madison Fire Department -- finished soon.

###Links###
----
- [View Project](http://www.madsafety.nwsmkr.com/incidents/)
- [Read Walkthrough](http://www.chrislkeller.com/introducing-madcrime-a-django-based-scraper-o)
- [View on GitHub](https://github.com/chrislkeller/madcrime)

###Install & Run The Scraper###
----
Download the zip file or fork the repo. Cd to your project directory and run pip install -r requirements.txt. I've been using the following for madcrime:

    BeautifulSoup==3.2.1
    Django==1.4
    South==0.7.5
    django-haystack==2.0.0-beta (Needed to solve an issue I ran into. Your mileage may vary.)
    geopy==0.94.2
    haystack==0.15
    mechanize==0.2.5
    mimeparse==0.1.3
    python-dateutil==1.5
    virtualenv==1.7.1.2
    virtualenv-clone==0.2.4
    virtualenvwrapper==3.5
    wsgiref==0.1.2
    yolk==0.4.3

Add the following to INSTALLED_APPS in settings.py:

	'madcrime',
	'haystack',

Add the following to settings.py:

	HAYSTACK_CONNECTIONS = {
		'default': {
			'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
		},
	}

Add the following to urls.py:

	(r'^incidents/', include('madcrime.urls')),

Run python manage.py syncdb from your project directory.

To scrape run python manage.py scrapepd from your project directory. You will be asked which page you want to scrape. Enter 1 to the first page, etc.

- Run python manage.py runserver and navigate to /incidents, and hopefully you see a list of incidents.

- The scraper is located in madcrime/management/commands/scrapepd.py

###Ideas to take this further###
----
####User Improvements####
- Improve basic search to include plain text, search by date, search by incident type, search by address or search by radius.
- <del>Add basic search capabilities.</del>
- <del>Add pop up when user clicks on incident map.</del>
- Add map and pop ups to search results page.
- Filter map markers on the incidents page by similar criteria.
- Add incident reports from the Madison Fire Department.
- Determine if content from Madison's Most Wanted and CrimeStoppers has a place.
- Determine how to handle cases that aren't posted.
- <del>Add map to main page with markers locating where incidents occured.</del>
- Add map with aldermanic ward polygons.
- Alert system for when new incidents are loaded.
- Hook in with Wis Circuit Court Access queries?
- <del>Table view should appear in descending order.</del>
- Search of incident table using datatables jQuery plugin.
- <del>Sorting of incident table using tablesorter or datatables jQuery plugins.</del>
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