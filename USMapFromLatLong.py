__author__ = 'glassman'
import matplotlib
matplotlib.use('Agg')

from mpl_toolkits.basemap import Basemap
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import csv

from itertools import *

def PlotMap(oldLon,oldLat,diffLon,diffLat):
    #request section of Basemap in latitude longitude box
    m = Basemap(llcrnrlon= -121.5,\
                llcrnrlat=24, \
                urcrnrlon= -65, \
                urcrnrlat = 46.5, \
                resolution = 'l', \
                projection = 'tmerc', \
                lon_0 = -100, \
                lat_0 = 37)

    fig = plt.figure()
    canvas = FigureCanvas(fig)
    m.ax = fig.add_axes([0, 0, 1, 1])
    fig.set_size_inches((6/m.aspect, 8.))

    #generate map with coasts, countries, state boarders
    m.drawmapboundary(fill_color='white')
    m.drawcoastlines(color='black')
    m.drawcountries(color='black')
    m.drawstates(color='black')

    #generate empty lats and longs lists
    latsList=[]
    lonsList=[]

    #Import previously generated Tracks CSV File, Write to a new list of lats and longs
    # with open(csvname) as csvfile:
    #     spamreader = csv.reader(csvfile, delimiter=',')
    #     for row in spamreader:
    #         list(row)
    #         lons = float(row[0])
    #         lonsList.append(lons)
    #         lats = float(row[1])
    #         latsList.append(lats)


    #plot tracking lists onto map
    x1, y1 = m(oldLon, oldLat)
    x2,y2 = m(diffLon,diffLat)
    m.scatter(x1, y1,c='r')
    m.scatter(x2,y2,c='b')

    #Annotate
    #These are currently too small on a 6" tall piece of metal, so they're
    #being removed until a larger version is in use.

    """
    for oddAnnotate,xOddStops,yOddStops,evenAnnotate,xEvenStops,yEvenStops in izip_longest(annotations[0::2],xstops[0::2],ystops[0::2],annotations[1::2],xstops[1::2],ystops[1::2]):
    #This is necessary because looping consecutively through xstops and ystops twice returns TypeError: 'float' object has no attribute '__getitem__'.  This generates six lists temporarily in the scope of the for loop.
        plt.annotate(oddAnnotate,xy=(xOddStops,yOddStops),xytext=(xOddStops,yOddStops+40000),fontsize='10',horizontalalignment=
                    'center', verticalalignment='bottom',backgroundcolor='white')
        if evenAnnotate == None:
            break
        plt.annotate(evenAnnotate,xy=(xEvenStops,yEvenStops),xytext=(xEvenStops,yEvenStops-70000),fontsize='10',horizontalalignment=
                    'center', verticalalignment='top',backgroundcolor='white')
    """
    #Probably the more correct way to do things, where [::2] gives odds starting with index [0] and [1::2] gives evens starting with index [1]
    """
    for name,xstops,ystops in zip(annotations[1::2],xstops[1::2],ystops[1::2]):
        plt.annotate(name,xy=(xstops,ystops),xytext=(xstops,ystops-70000),fontsize='6.75',horizontalalignment=
                    'center', verticalalignment='top',backgroundcolor='white')
    """

    canvas.print_figure('mapUS.png', dpi=200)
