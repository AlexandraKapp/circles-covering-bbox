# circles-covering-bbox

A script to get all circle center coordinates, of all circles needed to cover the area of a bounding box. 

Some APIs only allow queries bound to maximum radius. In order to get all items within a larger area than the max. radius multiple queries are necessary. 
This script gets all needed circle centers for a given bounding box and radius.

Set radius and bounding box in _get_circle_centers.py_ accordinly and run the script. The centers will be saved to _centers.csv_. 
To check the returned coordinates visually, ajust the radius in _view_circles_on_map.html_ and add your mapbox access token and open in a browser.

 ![](example.PNG)

(This script is only usable for rather small areas (e.g. a city), as always the the same latitude is used to calculate all longitudes. For larger areas the longitude needs to be calculated according to the proper latitude.)