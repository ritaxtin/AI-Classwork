from numpy import *;
from matplotlib import pyplot as plt;
import pylab;


def plotdata():
 
    plt.xlabel("the value of x")
    plt.ylabel("the value of y")
    loaddata()
    plt.show()

def loaddata():
    myfile = loadtxt("data.txt" ,delimiter = ',')
    x = myfile[:,0]
    y = myfile[:,1]
    plt.bar(x,y)
plotdata()
