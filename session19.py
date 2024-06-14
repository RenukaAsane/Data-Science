# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 09:06:59 2024

@author: Admin
"""
##################################################
'''Histogram'''
##################################################

import matplotlib.pyplot as plt
blood_Sugar=[113,85,90,150,149,88,93,115,135,80,77,82,129]
plt.hist(blood_Sugar,rwidth=0.8)#by default number of bins is set to 10
plt.hist(blood_Sugar,rwidth=0.5,bins=4)

'''
Histogram showing normal ,pre-diabetics patients distribution

80-100 : Normal
100-125 : Pre-diabetics
125 onwards : Diabetics
'''
plt.xlabel("Sugar Level")
plt.ylabel("Number of Patients")
plt.title("Blood Sugar Chart")

plt.hist(blood_Sugar, bins=[80,100,125,150], rwidth=0.95,color='green')

###########################################
'''Boxplot'''
'''In  boxplot dots are called outliers'''

#import libraries
import matplotlib.pyplot as plt
import numpy as np

#Create dataset
np.random.seed(10)
data = np.random.normal(100,20,200)

fig = plt.figure(figsize =(10,7))
#Creating plot
plt.boxplot(data)
#show plot
plt.show()
#################################################
#Multiple Boxplot

#import libraries
import matplotlib.pyplot as plt
import numpy as np

#Create dataset
np.random.seed(10)
data_1 = np.random.normal(100,10,200)
data_2 = np.random.normal(90,20,200)
data_3 = np.random.normal(80,30,200)
data_4 = np.random.normal(70,40,200)
data = [data_1,data_2,data_3,data_4]

fig = plt.figure(figsize=(10,7))
#Creating axes instance
ax = fig.add_axes([0,0,1,1])
#Creating plot
pb = ax.boxplot(data)
#show plot
plt.show()


  
