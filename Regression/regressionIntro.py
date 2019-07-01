#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 12:14:37 2019

@author: skhalil
"""

import numpy as np
import scipy as scp
import matplotlib.pyplot as plt
import math
datafile = open("LinearData.txt",'r')
data = [ [float(word) for word in line.split()] for line in datafile.readlines()]
print(data[0])

n = float(len(data))
print (n)

datafile.close()
dataX = [XY[0] for XY in data]
dataY = [XY[1] for XY in data]
print(dataX[0],dataY[0])

# find average
xbar = sum(dataX)/n
ybar = sum(dataY)/n

print("Average X: ",xbar," AverageY: ",ybar)

# find variance
varianceX = sum([pow(x-xbar,2) for x in dataX])/(n-1)
varianceY = sum([pow(y-ybar,2) for y in dataY])/(n-1)

# find standard deviation
stdevX = math.sqrt(varianceX)
stdevY = math.sqrt( varianceY )

print("x variance:", varianceX, "  x standard deviation:", round(stdevX,3))
print("y variance:", varianceY, "  y standard deviation:", round(stdevY,3))

covariance = sum( [(x-xbar)*(y-ybar) for x,y in zip(dataX,dataY)] ) / n
correlation = covariance/(stdevX*stdevY)
print("covariance:", round(covariance,3), "  correlation:", round(correlation,3))

def splot(dataX,dataY):
        fig = plt.figure()
        ax = plt.subplot(111)
        ax.scatter(dataX, dataY,label='data')
        plt.title('Some Very Attractive Title')
        plt.xlabel('x')
        plt.ylabel('y')
        axes = plt.gca()
        axes.set_xlim([0,18])
        axes.set_ylim([0,190])
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=False, ncol=2)
        fig.patch.set_facecolor('white') #sets the color of the border
        plt.show()
        
splot(dataX,dataY)

def hplot(data, nbins, label=''):
        fig = plt.figure()
        ax = plt.subplot(111)
        ax.hist(data,nbins,color='green',alpha=0.8)
        plt.title('Histogram')
        plt.xlabel(label)
        fig.patch.set_facecolor('white') #sets the color of the border
        plt.show()

hplot(dataY,10)

# least square
dataX2 = [x*x for x in dataX]
dataY2 = [y*y for y in dataY]
dataXY = [x*y for x,y in zip(dataX,dataY)]

m = ( sum(dataXY)*n - sum(dataX)*sum(dataY)  )/( sum(dataX2)*n - pow(sum(dataX),2)  )

b = ( sum(dataY)*sum(dataX2) - sum(dataX)*sum(dataXY) )/( sum(dataX2)*n - pow(sum(dataX),2)  )

print("m: ",round(m,3),"  b: ",round(b,3))

linX = range(20)
linY = [m*x+b for x in linX]

#over lay the fitted line

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(dataX, dataY,label='data')
ax.plot(linX, linY, color='red', label='Fit Line',linewidth=4.0)##New: fit line
plt.title('Least Square fit to the data')
plt.xlabel('x')
plt.ylabel('y')
axes = plt.gca()
axes.set_xlim([0,18])
axes.set_ylim([0,190])
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=False, ncol=2)
fig.patch.set_facecolor('white')
plt.show()

# residuals

SS_residuals = sum( [pow(y - (m*x+b),2) for x,y in zip(dataX,dataY) ]  )
SS_total = sum([pow(y-ybar,2) for y in dataY])
R_squared = 1.0 - (SS_residuals/SS_total)
print(round(R_squared, 4))  

# plot the residuals

residuals = [y - m*x+b for x,y in zip(dataX,dataY) if x < 4]
hplot(residuals,15)

perp_dist = [ (y - (m*x+b))/math.sqrt(1.0+m*m) for x,y in zip(dataX,dataY) ]

hplot(perp_dist,25)



      