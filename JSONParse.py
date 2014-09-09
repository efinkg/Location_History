__author__ = 'glassman'
import json
import csv

import datetime
import json
import pytz
import math

from os import path
import csv
def coordUnique(outputName, dataFileName, idfun=None):

    #outputFile = str(outputName)

    with open(dataFileName) as json_data:
        data = json.load(json_data)

    locations = data['locations']

    writer = csv.writer(open(outputName, "wb"))
    outputList = []

    temp = 1
    # order preserving
    if idfun is None:
        def idfun(x): return x
    seen = {}

    coordList = []
    timeList = []
    for x in locations:
        #print pytz.UTC.localize(datetime.datetime.fromtimestamp(int(x["timestampMs"])
        #print the timestamp in local timezone

        latitude = float(x['latitudeE7']) / 10000000
        longitude = float(x['longitudeE7']) / 10000000
        time = (
            pytz.UTC.localize(
                datetime.datetime.fromtimestamp(int(x["timestampMs"]) / 1000)))

        # but in new ones:

        #Prevent duplicates
        roundedLat = '%.10f' % (latitude)    #Rounds to 6 decimals
        roundedLon = '%.10f' % (longitude)
        if roundedLat in seen:
            continue
        if roundedLon in seen:
            continue

        seen[roundedLat] = 1
        seen[roundedLon] = 1

        if temp == 0:
            tempDistance = distance(latitude,longitude,(coordList[-1])[1],(coordList[-1])[0])
            #print tempDistance
            tempTime = hours(time,timeList[-1])

            if tempTime>0:
                speed = velocity(tempTime,tempDistance)

            if speed > 5:
                if speed < 100:
                    writer.writerow([longitude, latitude])
                    outputList.append((longitude,latitude))
                    #coordList.append([longitude, latitude])
                    #timeList.append(time)


        coordList.append([longitude, latitude])
        timeList.append(time)

        temp = 0

    #coordNearby(coordList,outputName)
    return outputList
    #return nearbyCoordList


def distance(lat1, lon1, lat2, lon2):
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c
    return d

def hours(time1, time2):
    diff = time2 - time1
    seconds = diff.total_seconds()
    hour = seconds/3600
    return hour

def velocity(tempTime, tempDistance):
    v = tempDistance/tempTime
    return v

# def coordNearby(coordList, outputName, idfun=None):
#     writer = csv.writer(open(outputName, "wb"))
#
#     # order preserving
#     if idfun is None:
#         def idfun(x): return x
#     seen = {}
#     nearby = {}
#     for x in coordList:
#         #Prevent places I barely stopped in
#         nearbyLat = '%.10f' % (int(x[0]))    #Rounds to 6 decimals
#         nearbyLon = '%.10f' % (int(x[1]))
#
#         nearby[nearbyLat] = 1
#         nearby[nearbyLon] = 1
#
#     for x in coordList:
#         #Prevent places I barely stopped in
#         nearbyLat = '%.10f' % (int(x[0]))    #Rounds to 6 decimals
#         nearbyLon = '%.10f' % (int(x[1]))
#
#         #print([x[0], x[1]])
#
#         if nearbyLat not in nearby:
#             continue
#         if nearbyLon not in nearby:
#             continue
#
#         writer.writerow([x[0], x[1]])
#
# #listCoords = coordUnique(getData()) #Find unique coordinates to 4 decimal places of my json
# #nearbyCoords = coordNearby(listCoords)