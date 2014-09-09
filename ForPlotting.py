__author__ = 'glassman'

def seperateLatLong(list):
    outputLonList = []
    outputLatList = []
    for item in list:
        outputLonList.append(item[0])
        outputLatList.append(item[1])

    return (outputLonList,outputLatList)