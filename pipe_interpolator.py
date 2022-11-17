from scipy import interpolate
import matplotlib.pyplot as plt
from numpy import arange 


def createInterpolator():
    x = [10,15,25,40,65,100,150,250,400,650,1000,1500,2500,4000,6500,10000,15000,25000,40000,65000,100000]
    y = [2.03,1.92,1.78,1.66,1.54,1.45,1.36,1.26,1.18,1.10,1.03,0.97,0.9,0.84,0.78,0.73,0.69,0.64,0.595,0.555,0.520]
    f = interpolate.interp1d(x,y,"cubic")
    return f

def testInterpolator(f):
    x = [10,15,25,40,65,100,150,250,400,650,1000,1500,2500,4000,6500,10000,15000,25000,40000,65000,100000]
    y = [2.03,1.92,1.78,1.66,1.54,1.45,1.36,1.26,1.18,1.10,1.03,0.97,0.9,0.84,0.78,0.73,0.69,0.64,0.595,0.555,0.520]
    f = interpolate.interp1d(x,y,"cubic")
    xnew = arange(10, 100000, 2)
    ynew = f(xnew)
    plt.plot(x, y, 'o', xnew, ynew, '-')
    plt.show()


