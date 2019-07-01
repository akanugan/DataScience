#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 13:24:05 2019

@author: skhalil
"""

###################################################
#  Filename : linear_regression_scikit            #
#  Purpose : To demonstrate simple linear regress #
#   using the sklearn library                     #
#            1. Create Predictive Model           #
#            2. Visualize the Model Performance   #
#  Author : Niel S.                               #
#  The English Tea Company LLC                    #
###################################################


from matplotlib import pyplot as plt
from sklearn import linear_model, metrics
#The Dataset.

#These are the values of the independent variable.
X = [108,19,13,124,40,57,23,14,45,10,5,48,11,23,7,2,24,6, \
    3,23,6,9,9,3,29,7,4,20,7,4,0,25,6,5,22,11,61,12,4,16,13,60,\
    41,37,55,41,11,27,8,3,17,13,13,15,8,29,30,24,9,31,14,53,26]

#These are the values of the dependent variable
Y = [392.5,46.2,15.7,422.2,119.4,170.9,56.9,77.5,214,65.3, \
    20.9,248.1,23.5,39.6,48.8,6.6,134.9,50.9,4.4,113,14.8, \
     48.7,52.1,13.2,103.9,77.5,11.8,98.1,27.9,38.1,0,69.2,14.6, \
     40.3,161.5,57.2,217.6,58.1,12.6,59.6,89.9,202.4,181.3,152.8, \
     162.8,73.4,21.3,92.6,76.1,39.9,142.1,93,31.9,32.1,55.6,133.3, \
     194.5,137.9,87.4,209.8,95.5,244.6,187.5]


def main():
    #Visualizing the data.
    visualize_input_data(X,Y)
    #Obtain the coefficients of regression
    X_t,Y_t,Y_mdl,A, B = linear_regression(X,Y)
    #Let us visualize the model's performance
    visualize_trained_model(X_t,Y_t,Y_mdl,A,B)
    
    plt.show()
        
def linear_regression(X,Y):
    '''
    Input Parameters:
     X : 1D list of independent values.
     Y : 1D list of dependent values.
    '''
    #Change the row format [a,b,c] to column format [[a],[b],[c]]
    X_train =[[x] for x in X[0:25] ]
    X_test  =[[x] for x in X[25:]  ]
    Y_train =[[y] for y in Y[0:25] ]
    Y_test  =[[y] for y in Y[25:]  ]

    #Creating an instance of LinearRegression       
    reg = linear_model.LinearRegression()

    #Train the model using training sets.
    reg.fit(X_train,Y_train)

    #Use test set to make predictions.
    Y_mdl = reg.predict(X_test).tolist()

    #The slope and The Intercept
    a = reg.coef_[0][0]
    b = reg.intercept_[0]

    #Restore back from column format to row format.
    X_test = [x[0] for x in X_test]
    Y_test = [y[0] for y in Y_test]
    Y_mdl  = [y[0] for y in Y_mdl]
    return X_test,Y_test,Y_mdl,a,b


def visualize_trained_model(X_test,Y_test,Y_mdl,A,B):
    '''
    Publish a 2-D scatterplot between
    X and Y overlaid with the straight 
    line : A*x+B = Y
    '''
    #Create a figure object
    fig0,(ax0,ax1,ax2) = plt.subplots(1,3,figsize=(15,5))
    ##Do a scatter plot for the variables.
    ax0.scatter (X_test,Y_test,color='black',label='Test Data')
    
    #Set axes labels
    ax0.set_xlabel('X')
    ax0.set_ylabel('Y')
    
    #Set axes ranges
    ax0.set_xlim([0,50])
    ax0.set_ylim([0,130])
    
    ##Now is the time to generate the regression line.    
    A = round(A,2)
    B = round(B,2)
    X_line = [i for i in range(0,35)]
    Y_line = [A*x+B for x in X_line]
    ax0.plot(X_line,Y_line,label = str(A)+'*x'+'+'+str(B))
    #Erase the verticle frame spines
    ax0.spines['right'].set_color('none')
    ax0.spines['top'].set_color('none')
    #Draw Legend
    ax0.legend()
    
    #ax0.spines['right'].set_color('none')
    #ax0.spines['top'].set_color('none')
    
    ax1.spines['right'].set_color('none')
    ax1.spines['top'].set_color('none')
    
    ax2.spines['right'].set_color('none')
    ax2.spines['top'].set_color('none')
   
    ##Let us look at the modeling errors: residuals.
    Y_errors = [(y_mdl-y_test)/y_test  if y_test > 0 else 0 for y_test,y_mdl in zip(Y_test, Y_mdl)]
    Y_errors_rms = round ( sum([e*e for e in Y_errors]) / len(Y_errors),2)
    
    ##A histogram of the residuals.
    err_min,err_max,binw = -0.5,0.5,0.05
    nbins = int ((err_max-err_min)/binw)+1
    bins  = [err_min+i*binw for i in range(0,nbins)]
    ax1.hist(Y_errors,bins=bins,label='RMS Error: '+str(Y_errors_rms))
    #Set axes labels
    ax1.set_xlabel('Relative Error')
    ax1.set_ylabel('Frequency')
    #Erase the spines
    ax1.spines['right'].set_color('none')
    ax1.spines['top'].set_color('none')
    #Draw the legend
    ax1.legend()
    
    ##How do the residuals distribute across X?
    ax2.scatter(X_test,Y_errors)
    #Set axes labels
    ax2.set_xlabel('X')
    ax2.set_ylabel('Relative Error')
    #Erase the spines
    ax2.spines['right'].set_color('none')
    ax2.spines['top'].set_color('none')
    
     
    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f'% metrics.r2_score(Y_test, Y_mdl))

    
    
    
    fig0.suptitle('Linear Regression')

    
def visualize_input_data(X,Y):
    '''
    Input:
     X : a column of x values.
     Y : a column of y values. 
    '''
    
    #Create a figure object with 3 axes.
    fig0,(ax0,ax1,ax2) = plt.subplots(1,3,figsize=(15,5))
    
    #How many bins we need for histograming?
    max_range = 150
    min_range = 0
    bin_width = 15
    ####Number of bins
    nbins =int((max_range-min_range)/bin_width)
    ####Bins
    bins = [0+i*bin_width for i in range(0,nbins+1)]
   
    #Create the histogram a.k.a frequency chart of X    
    n0,b0,p0 = ax0.hist(X,bins=bins,histtype='stepfilled',label='X',color='blue')
    
    #Create a histogram of Y (same binning as in X). 
    n1,b1,p1 = ax1.hist(Y,bins=bins,histtype='stepfilled',label='Y',color='orange')
   
    #Some Cosmetic settings for ax0
    ax0.set_xlabel('X')
    ax0.set_ylabel('Frequency')
    ax0.legend()
    
    #Some Cosmentics settings for ax1
    ax1.set_xlabel('X')
    ax1.set_ylabel('Frequency')
    ax1.legend()

    ##Do a scatter plot for the variables.
    ax2.scatter (X,Y,label='Claims Vs Amount')
    
    #Set axes labels
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    
    #Set axes ranges
    ax2.set_xlim([0,50])
    ax2.set_ylim([0,130])
    
    #Display the legend
    ax2.legend()
    
    
    #Set a figure title
   
    fig0.suptitle('Input Variables')
 
   
    
    
if __name__ == '__main__':
    main()
