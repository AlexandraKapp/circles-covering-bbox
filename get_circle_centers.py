import math
from itertools import permutations, repeat
import numpy as np

# set radius in meters (e.g. here 5 km)
radius = 5000

# set bounding box (e.g. here Berlin)
start_lat = 52.341823
start_long = 13.088209
end_lat = 52.669724
end_long = 13.760610

# number of km per degree = 40075km / 360 = ~111
# (between 110.567km at the equator and 111.699km at the poles)
# 40075 km earths perimeter at equator
# 1km in degree = 1 / 111.32 = 0.0089
# 1m in degree = 0.0089 / 1000 = 0.0000089

one_meter_in_degree = 1 / 111.32 / 1000
coef = 2*radius * one_meter_in_degree

# distance between all latitudes always the same
def get_new_lat(old_lat):
    return (old_lat + coef)

# pi / 180 = 0.018
# distance between longitudes depends on latitude
# This script is only usable for rather small areas (e.g. a city), as always the start_lat is used to calculate new longs!
# For larger areas a the longitude needs to be calculated according to the proper lat!
def get_new_long(old_long):
    return (old_long + coef / math.cos(start_lat * (math.pi / 180)))

# get all lats:
first_row_lats = []
second_row_lats = []
current_lat1 = start_lat
current_lat2 = start_lat + radius * one_meter_in_degree
while current_lat1 < end_lat:
    first_row_lats.append(current_lat1)
    second_row_lats.append(current_lat2)
    current_lat1 = get_new_lat(current_lat1)
    current_lat2 = get_new_lat(current_lat2)

# get all longs:
first_row_longs = []
second_row_longs = []
current_long1 = start_long
current_long2 = start_long + (radius * one_meter_in_degree) / math.cos(start_lat * 0.018)
while current_long1 < end_long:
    first_row_longs.append(current_long1)
    second_row_longs.append(current_long2)
    current_long1 = get_new_long(current_long1)
    current_long2 = get_new_long(current_long2)

all_coordinates = np.array([]).reshape(0,2)
for long in first_row_longs:
    coordinates = np.array(list(zip(first_row_lats, np.repeat(long, len(first_row_lats)))))
    all_coordinates = np.append(all_coordinates, coordinates, axis = 0)

for long in second_row_longs:
    coordinates = np.array(list(zip(second_row_lats, np.repeat(long, len(second_row_lats)))))
    all_coordinates = np.append(all_coordinates, coordinates, axis = 0)

# save radius centers to csv
np.savetxt("centers.csv", all_coordinates, header= 'lat, long', delimiter=",", fmt="%10.6f")