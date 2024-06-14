# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 08:24:40 2024

@author: Admin
"""
################################################33
'''SEABORN'''
###################################################3

import seaborn as sns
import pandas as pd

Cars=pd.read_csv("c:/1-python/Cars.csv")
Cars.head()
Cars.columns


sns.relplot(x='HP',y='MPG',data=Cars)
sns.relplot(x='HP',y='MPG',data=Cars,kind='line')


sns.relplot('Sales','Profit',data=Cars)
sns.relplot('Sales','Profit',data=Cars,hue='order priority')
sns.relpot('Order Data','Sales',data=Cars,kind='line')

##################################################
'''Boxplot'''

sns.catplot(x='HP', y='MPG',data=Cars,kind='box')

#Histogram
sns.distplot(Cars.HP)
########################################
########################################

#multiple correlation regression analysis
#Exploratory data analysis
#1. Measure the central tentency
#2. Measure the dispersion
#3. Third moment business decision
#4. Forth moment business decision
#5. Probability distribution
#6. Graphical representation (Histogram,Boxplot)
Cars.describe()
#Graphical Representaion
import matplotlib.pyplot as plt
import numpy as np

plt.bar(height=Cars.HP,x=np.arange(1,82,1))
sns.distplot(Cars.HP)
#data in right skewed
sns.boxplot(Cars.HP)
#their are several outlier in HP columns
#simpilar operations are expected for other three columns
sns.distplot(Cars.MPG)
#data is slightlt left distribution
plt.boxplot(Cars.MPG)
#There are no outlier
sns.distplot(Cars.VOL)
#Data is slighted left distributed
plt.boxplot(Cars.VOL)
sns.distplot(Cars.SP)
#Data is slighted left distributed
plt.boxplot(Cars.SP)
#there are severasl outlier
sns.distplot(Cars.WT)
plt.boxplot(Cars.WT)

##############################################
#join plot
import seaborn as sns
sns.jointplot(x=Cars['HP'],y=Cars['MPG'])

###########################################
#count plot
#countplot shows how many times each value occured
#92 HP value occured 7 times
plt.figure(1,figsize=(16,10))
sns.countplot(Cars['HP'])

