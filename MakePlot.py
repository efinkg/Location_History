__author__ = 'glassman'

import JSONParse
import USMapFromLatLong
import DifferentPlaces
import ForPlotting

Locations1 = "AllPlaces.csv"
Locations2 = "AllPlaces_new.csv"
Locations3 = "NewPlaces.csv"
JSON1 = "LocationHistory.json"
JSON2 = "LocationHistory_new.json"

oldList = JSONParse.coordUnique(Locations1,JSON1)
newList = JSONParse.coordUnique(Locations2,JSON2)

diffList = DifferentPlaces.newPlaces(oldList,newList)
oldLon,oldLat= ForPlotting.seperateLatLong(oldList)
diffLon,diffLat = ForPlotting.seperateLatLong(diffList)

# oldLon,oldLat= ForPlotting.seperateLatLong(oldList)
# newLon,newLat= ForPlotting.seperateLatLong(newList)
#
# diffLon = DifferentPlaces.newPlaces(oldLon,newLon)
# diffLat = DifferentPlaces.newPlaces(oldLat,newLat)

USMapFromLatLong.PlotMap(oldLon,oldLat,diffLon,diffLat)