from math import radians, cos, sin, asin, sqrt, floor

def haversine(point1, point2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1= point1[0]
    lon2= point2[0]
    lat1= point1[0]
    lat2= point2[0]
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    return km


coordinate_bike= (52.535207, 13.395619)
location = ( 52.537061, 13.394832)
destination = (52.525076, 13.392270)

velo_foot = 5
velo_bike = 15

distance_to_bike = haversine(location, coordinate_bike)

distance_bike_destination = haversine(coordinate_bike, destination)

distance_to_destination = haversine(location,destination)

time_foot = floor((distance_to_destination/velo_foot)*60)
time_bike = floor((distance_to_bike/velo_foot+ distance_bike_destination/velo_bike)*60)

if (time_foot<time_bike):
		print ("Gehe zu Fuss: %s min" %time_foot)
else:
		print ("Nehme das Fahrrad: %s min" %time_bike)