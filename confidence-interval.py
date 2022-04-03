# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 15:26:42 2021

@author: srpdo
"""
import numpy as np
import matplotlib.pyplot as plt


#the functions returns the [mean, standart deviation] of the given list
def estimate(alist):
    pointEstimator = np.mean(alist)
    std = np.std(alist)
    marginOfError = 1.96*std/np.sqrt(len(alist))
    return [pointEstimator, marginOfError]

data_0 =  np.loadtxt("data5.txt")               #creates a list containing the rows of the txt file


prices=[]                                       #will hold the price values
sizes=[]                                        #will hold the size values 


#fills the price and size values
for i in range(len(data_0)):
    prices.append(data_0[i][1])             #second column of every line is price data 
    sizes.append(data_0[i][2])              #third column of every line is size data
    

 
#turning both arrays into numpy arrays, to be able to make a division between them later on

prices=np.array(prices)             #*1000 TL
sizes = np.array(sizes)             #m^2


pricePerSize=np.array(prices/sizes)     #a numpy array holding the price/size values

priceEstimation_prices = estimate(prices)[0]                                 

#estimator finds the estimated price/size value, multiplying it with the average size to find the
#point estimator of price
princeEstimation_pricePerSize = estimate(pricePerSize)[0]*np.mean(sizes)

#printing the results
print("Average selling price (using prices only) is ", priceEstimation_prices) 
print("Average selling price (using price/size) is ", princeEstimation_pricePerSize)


l_bound = estimate(prices)[0] - estimate(prices)[1]         #lower bound for the 95% confidence interval
u_bound = estimate(prices)[0] + estimate(prices)[1]         #upper bound for the 95% confidence interval

#printing the results
print("95% confidence interval for prices : {:.4f} ± {:.4f}".format(estimate(prices)[0],estimate(prices)[1]))
print("95% confidence interval for prices : {:.4f} < m < {:.4f}".format(l_bound,u_bound))


#ploting the histogram
plt.hist(prices)
plt.title("Histogram of Selling Prices")
plt.xlabel("Prices (k TL)")
plt.show()
    