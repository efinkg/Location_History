__author__ = 'glassman'

def newPlaces(oldList,newList):
    diff = set(newList)-set(oldList)
    diffList = list(diff)
    return diffList