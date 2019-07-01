#! /usr/bin/python

#####################################################################################################################
######################################### Oridinary Least Square Regression #########################################
######################################### --------------------------------- #########################################
# a model that predicts the behaviour of a dependent variable (yi) for every independent varaible (xi) described by a
# line equation yi = b0+b1*xi+ei, where b0 is called slope, b1 is called yi intercept and ei is the error that lies
# between the yi and xi relation. The goal is to find the estimated values b^0 and b^1 that provides the "best" fit
# for the data points. The "best" fit here means a line that minimize the sum of squared residuals e^i, where
# e^i = yi-b^0-b^1*xi. Therefore, by expanding the objective funtion Q(b^0,b^1) = Sum( (e^i)^2 ) we estimate b^0 and
# b^1, where b^0 = mean(y) - b^1* mean(x), and b^1 = Cov(x,y)/Var(x)
######################################################################################################################

#import os, sys
import matplotlib.pyplot as plt
#import statistics as stats
from scipy import stats
import numpy as np


class linearRegression1D:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = np.size(x)
        self.xm = np.mean(x)
        self.ym = np.mean(y)
        
    def linearRegression1D_fit(self):     
        try:
            b0 = b1 = None
            xmean = self.xm 
            ymean = self.ym            
            bVar = np.var(self.x, ddof=1)
            bCov = np.cov(self.x, self.y, ddof=1)           
            # In numpy cov function, the return value is a matrix with cov of all elements, so pick the non-diagonal value            
            if bVar>0: 
                b1 = bCov.item((0,1))/bVar
                b0 = ymean - b1*xmean               
            return (b0, b1)
        except Exception as err:
            print (err)

    def linearRegression1D_predict(self, b0, b1):
        self.b0 = b0
        self.b1 = b1
        #print ("\nb0 = {} \nb1 = {} \nx = {}".format(self.b0, self.b1, x))
        y_pred = self.b0 + self.b1*self.x
        return y_pred

    def linearRegression1D_meanSquaredError(self, y_pred):
        self.y_pred = y_pred
        y_res = self.y - self.y_pred
        mse = np.sum([yi*yi for yi in y_res])/(self.n-2)
        return mse

    def LinearRegression1D_standardError(self, mse):
        try:
            xmean = self.xm
            self.mse = mse
            # mean squared deviation
            xdevsq = np.sum([ (xi-xmean)**2 for xi in self.x])
            if xdevsq>0 and self.n > 0:
                ret = []       
                for xi in self.x:
                    standardError = np.sqrt( self.mse * ( 1./self.n + (xi-xmean)**2/xdevsq ) )
                    ret.append(standardError)
                return ret
            return None
        except Exception as err:
            print (err)
    
        
#####
x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([2, 7, 8, 13, 14, 20, 19])

#x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

linreg = linearRegression1D(x, y)        

# get regression model parameters
b = linreg.linearRegression1D_fit()

# get the predicted response vector and residuals
y_fit = linreg.linearRegression1D_predict(b[0], b[1])

# get mean squared error/variance
mse = linreg.linearRegression1D_meanSquaredError(y_fit)

# get variance of each data point from the fitted line
y_fit_var = linreg.LinearRegression1D_standardError(mse)

# using student's t-distribution single tail, for n-2 dof, construct the upper and lower CI (95%)
ndof = len(x) - 2
t_crit = stats.t.ppf(1-0.05, ndof)

y_ci_low = [yi-t_crit*yvar for yi, yvar in zip(y_fit, y_fit_var)]
y_ci_hi  = [yi+t_crit*yvar for yi, yvar in zip(y_fit, y_fit_var)]

# print
print '\n inputs: ', '\n x: ', x, '\n y: ', y 
print '\n b0: ', b[0], '\n b1: ', b[1], '\n y_fit: ', y_fit, '\n mse: ', mse, '\n y_fit_var: ', y_fit_var, '\n ndof: ', ndof, '\n t_crit: ', t_crit, '\n y_ci_low: ', y_ci_low,  '\n y_ci_hi: ', y_ci_hi

# plot it
plt.scatter(x,y)
plt.plot(x,y_fit,'r--')
plt.plot(x,y_ci_low,'r')
plt.plot(x,y_ci_hi,'r')
plt.ylabel('Y-variable')
plt.xlabel('X-variable')
plt.title('Linear Regression')
#plt.show()
plt.savefig('linear_regression.png')
plt.savefig('linear_regression.pdf')


# ------------ Output -------------

# inputs:  
# x:  [1 2 3 4 5 6 7] 
# y:  [ 2  7  8 13 14 20 19]

# b0:  0.0 
# b1:  2.96428571429 
# y_fit:  [  2.96428571   5.92857143   8.89285714  11.85714286  14.82142857
#  17.78571429  20.75      ] 
# mse:  2.56428571429 
# y_fit_var:  [1.0911284179645384, 0.85595155308258541, 0.67668911862487213, 0.60524914755185322, 0.67668911862487213, 0.85595155308258541, 1.0911284179645384] 
# ndof:  5 
# t_crit:  2.01504837267 
# y_ci_low:  [0.76560917129319961, 4.2037876444487274, 7.529295835569167, 10.637536547309102, 13.457867264140598, 16.060930501591585, 18.551323457007484] 
# y_ci_hi:  [5.1629622572782292, 7.6533552126941302, 10.256418450145118, 13.076749166976613, 16.184989878716546, 19.510498069836984, 22.948676542992516]
 
# ------------ References ---------

# http://www.stat.uchicago.edu/~eichler/stat22000/Handouts/l23.pdf
# https://www.geeksforgeeks.org/linear-regression-python-implementation/
# https://www.linkedin.com/pulse/linear-regression-from-scratch-lovedeep-saini/
# https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
# mse: https://stats.stackexchange.com/questions/140536/whats-the-difference-between-the-variance-and-the-mean-squared-error
# standard error: http://www.real-statistics.com/regression/confidence-and-prediction-intervals/

# ----------- Definations that can be also caluclated using only numpy ------------

# var = np.sum( (xi - xmean)**2 for xi in self.x)/(n-1)   #OR
# var = (np.sum(xi**2 for xi in self.x) - n*(xmean**2))/(n-1) 
# cov = np.dot((self.x - xmean), (self.y - ymean))/(n-1)  #OR
# cov = (np.sum(xi*yi for xi, yi in zip(self.x, self.y))  - n*ymean*xmean)/(n-1)
