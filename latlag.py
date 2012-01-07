# -*- coding: utf-8 -*-

from optparse import OptionParser
from googlemaps import GoogleMaps
import sys
import math


def parse_options():
	"""
	-s:  departure
	-g:  destination
	"""
	usage = "%prog [-s] (point of departure)[-g] (destination)"
	parser = OptionParser(usage=usage)
	parser.add_option("-s", dest="departure", action="store", metavar="DEPARTURE", help="your point of departure")
	parser.add_option("-g", dest="destination", action="store", metavar="DESTINATION", help="your destination")

	(options, args) = parser.parse_args(sys.argv[1:])

	return options, args

def main():
	
	gmaps = GoogleMaps()
	options, args = parse_options()

	argvs = sys.argv
	argc = len(argvs)

	if argc != 5:
		print("Wrong number of arguments")
		sys.exit()
	else:
		departure = options.departure
		destination = options.destination
		earth_r = 6378.18

		start_lat, start_lag = gmaps.address_to_latlng(departure)
		goal_lat, goal_lag = gmaps.address_to_latlng(destination)

		if start_lat < goal_lat:
			dig2rag_num = start_lat
		else:
			dig2rag_num = goal_lat

		dif_lat = math.radians(abs(start_lat - goal_lat))
		dif_lag = math.radians(abs(start_lag - goal_lag))

		nsdist = earth_r * dif_lat
		ewdist = earth_r * math.cos(math.radians(dig2rag_num)) * dif_lag

		dist = math.sqrt(nsdist**2 + ewdist**2)

		"""Debug
		print(dif_lat)
		print(dif_lag)
		print(nsdist)
		print(ewdist)
		"""
		print
		print("Departure   : %s\t (latitude : %s, longitude : %s)" % (departure, start_lat, start_lag))
		print("Destination : %s\t (latitude : %s, longitude : %s)" % (destination, goal_lat, goal_lag))
		print("Distance    : %f km" % dist)
		print

if __name__ == "__main__":
	main()
