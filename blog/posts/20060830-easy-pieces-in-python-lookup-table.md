# Easy Pieces in Python: A Lookup Table

_August 30, 2006_  
Originally published at `https://digitalhistoryhacks.blogspot.com/2006/08/easy-pieces-in-python-lookup-table.html`

Often you find yourself with data that would be more useful in another form. For example, you might have a list of zip codes that you want to plot with Google Maps[^1]. Unfortunately, the Google Maps API only takes latitude and longitude. There is an online table of zip codes[^2] with cities, states, latitudes and longitudes at the US Census Bureau website, however. With a little bit of Python[^3] it is easy to convert your zip codes to latitude and longitude.  
  
A line in the online data table looks like this:  
> "06","91436","CA","ENCINO",118.488238,34.15098,13605,0.000457

  
If we split each line apart at the commas, we will end up with eight fields. Since Python counts from zero, this means the zip code is field number 1. The longitude and latitude are fields 4 and 5 respectively. Our script reads in the data file a line at a time, then creates a dictionary so we can look up each zip code and get a string representing the latitude and longitude. (For Google Maps, we want latitude first, and longitude expressed as a negative number.)  
 `datafile = open('zips.txt', 'r')  
lookup = {}  
for line in datafile.readlines():  
    items = line.split(',')  
    zip = items[1]  
    lat = items[5]  
    lon = items[4]  
    lookup[zip[1:-1]] = "%s, -%s" % (lat, lon)`  
We now can look up individual zip codes:  
 `print lookup['91436']`  
returns  
> '34.15098, -118.488238'

  
Or we can transform all of our data at once:  
 `ziplist = ['02139', '02141', '02142', ...]  
print [lookup[z] for z in ziplist]`  
returns  
> ['42.364688, -71.104155', '42.370701, -71.088277', '42.362025, -71.083011', ...]

  
  
Tags: application program interface[^4] | geocoding[^5] | Google[^6] | munging[^7] | python[^8]

[Back to the blog archive](../README.md)

[^1]: `http://www.google.com/apis/maps/`
[^2]: `http://www.census.gov/tiger/tms/gazetteer/zips.txt`
[^3]: `http://www.python.org`
[^4]: `http://technorati.com/tag/application+program+interface`
[^5]: `http://technorati.com/tag/geocoding`
[^6]: `http://technorati.com/tag/Google`
[^7]: `http://technorati.com/tag/munging`
[^8]: `http://technorati.com/tag/python`
