# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 08:16:00 2024

@author: Admin
"""
#Shallow Copy and Deep Copy
#Shallow Copy:it is one level deep
#[1,2,3,4]:one level deep
#[[1,2,3,4]]:two level deep
#modify on level 1 does no affect
#use copy.copy()
import copy
list_a=[1,2,3,4,5]
list_b=copy.copy(list_a)

#not affect the other list
list_b[0]=-10
print(list_a)
print(list_b)
#o/p
#[1, 2, 3, 4, 5]
#[-10, 2, 3, 4, 5]

##################################
#it does not work on 2 level
#but with nested object,modifying on level 2
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]] 
list_b=copy.copy(list_a)

#affect the other
list_b[0][0]=-10
print(list_a)
print(list_b)
#output
#[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
#[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
#######################################

#Deep copy
#Full dependent clones.Use copy.deepcopy()
import copy
list_a=[[1,2,3,4,5,],[6,7,8,9,10]]
list_b=copy.deepcopy(list_a)
#not affect yhe other
list_a[0][0]=-10
print(list_a)
print(list_b)
#o/p
#[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
#[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

##############################################
import pandas as pd
f1=pd.read_csv('C:/1-python/buzzers.csv')

#########################################
#check for working directory

import os
with open('C:/1-python/buzzers.csv')as raw_data:
    print(raw_data.read())

############################################
#Reading CSV Data as lists
#reading the file 
import csv
with open('C:/1-python/buzzers.csv')as raw_data:
    for line in csv.reader(raw_data):
        print(line)

##########################################
#reading csv file in the form of dictionary
import csv
with open('buzzers.csv')as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)

##############################################
with open('buzzers.csv') as data:
    #ignore=data.readline()
    flights={}
    for line in data:
        k,v=line.split(',')
        flights[k]=v
flights

#####################################################
#pre-requisite to decorators
def plus_one(number):
    number1 = number+1
    return number1
plus_one(5)

#########################################################
#defining functions inside other function
def plus_one(number):
    
    def add_one(number):
        number1=number+1
        return number1
    result=add_one(number)
    return result
plus_one(4)

######################################################
#Passing functions as arguments to other function
def plus_one(number):
    result1=number+1
    return result1

def function_call(function):
    result=function(5)
    return result

function_call(plus_one)

##############################################
#function returning other function
def hello_function():
    def say_hi():
        return "Hellooo"
    return say_hi
hello=hello_function()
hello()

#################################################
#need of decorators:when repeated logic is used

import time
def calc_square(numbers):
    start=time.time()
    result =[] #empty list
    for number in numbers:
        result.append(number*number)
    end=time.time()
    total_time=(end-start)*1000
    #1000 is included because we wan result in milli second
    print(f"Total time for execution square is {total_time}")
    return result


def calc_cube(numbers):
    start=time.time()
    result = []
    for number in numbers:
        result.append(number*number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"Total time for execution cube is {total_time}")
    return result

array=range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)



    








    
