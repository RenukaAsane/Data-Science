# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 08:16:51 2024

@author: Admin
"""

###########################################

'''Python for data scence'''
'''Pandas-2types:-Series and Columns'''
#series:-Operation on 1 column
#a series is used to model 1 dimentional data
#similar to a list in python
#the series objet also has a few more bits
#of data,including an index and a name

import pandas as pd
songs2=pd.Series([145,142,38,13],name='counts')
#It is easy to inspect the index ogf a serial (or data)
songs2.index
#index can be string based as well,in
#which case pandas indicated
#that the datatype for the same index is obj(not string)

songs3=pd.Series([145,142,38,13],name='counts',
                 index=['Paul','John','George','Ringo'])
songs3.index
songs3

###################################################
#The NaN value
#this value stands for Not a Number
#and is usually ignored in arithmetic operations
#(similar to null in SQL)
#if u load data from a CSV file
#an empty value for an otherwise
#numeric column will become NaN
import pandas as pd
f1=pd.read_csv('age.csv')
f1

df=pd.read_excel('c:/1-python/Bahaman.xlsx')
#None,NaN,nan, and null are synonyms
#the series obj behaves similarly to a NumPy array
import numpy as np
numpy_ser = np.array([145,142,38,13])
songs3[1]
#142
numpy_ser[1]
#they both havew methods in common
songs3.mean()
numpy_ser.mean() 

####################################################
#Pandas series data structure provides
#support for the basic crud
#operations-creates ,read,update,delete
#creation
george=pd.Series([10,7,1,22],
index=['1968','1969','1970','1930'],
name="George_Songs")
george
#without index
george=pd.Series([10,7,1,22],
#index=['1968','1969','1970','1970'],
name="George_Songs")
george

###################################################################3
#reading
#to read or select the data fro  a series
george['1968']
george['1970']
#error

##############################################33333
#we can iterate over data in serries
#as well when iterating over series

#update
george['1969']=68
george['1970']
george

############################################
#3rd March 2024
#convert types
#string use.astype(str)
#numeric use pd.to_numeric
#integer use .astype(int),
#note that this will wail with NaN
#datetime use pd.to_datatype
songs_66=pd.Series([3,None,11,9],
index=['George','Ringo','John','paul'],
name='Counts')
songs_66.dtypes
#dtype('float64')
pd.to_numeric(songs_66.apply(str))
#there will be error
pd.to_numeric(songs_66.astype(str),errors='coerce')
#if we pass error='coerce'
#we see that it supports many formats
songs_66.dtypes
#dealing with None
#the .fillna method will replace them with the given value
songs_66=songs_66.fillna(-1)
songs_66=songs_66.astype(int)
songs_66.dtypes

##################
songs_66=pd.Series([3,None,11,9],
index=['George','Ringo','John','paul'],
name='Counts')
songs_66=songs_66.fillna(-1)
songs_66=songs_66.astype(int)
songs_66.dtypes 

#########################################3         
#NaN values can be dropped from 
#the series using  .dropna
songs_66=pd.Series([3,None,11,9],
index=['George','Ringo','John','paul'],
name='Counts')
songs_66=songs_66.dropna()
songs_66

#############################################
#append,combining, and joining two series
songs_69=pd.Series([7,16,21,39],
index=['Ram','Sham','Ghansham','Krishna'],
name='Counts')
#to concatenante 2 series together simple
#use .append method
songs=pd.concat([songs_66,songs_69])
songs

############################################
#ploting series
import matplotlib.pyplot as plt
fig = plt.figure()
songs_69.plot()
plt.legend()

##############################################3
fig = plt.figure()
songs_69.plot(kind='bar')
songs_66.plot(kind='bar',color='r')
plt.legend()

#histogram:-Distribution of data
import numpy as np
data = pd.Series(np.random.randn(500),name='500_random')
fig=plt.figure()
ax = fig.add_subplot(111)
data.hist()

###################################















