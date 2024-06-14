# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:13:37 2024

@author: Admin
"""
##############################################
#A python decorators is a function
#that takes in  afunction and
#returns it by adding some functionality
#in deploy tools decorators are used
def say_hi():
    return 'hello there'

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
decorate = uppercase_decorator(say_hi)
decorate()    

################################################
#however,python provides much easier
#way for use to apply decorators
#we use simply @ symbol before
#the function we'd like to decorate
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'
say_hi()

################################################
#Appling multiple Decorators 
#to a single function
#we can use multiple decorators to a single fun
#however,the decorators will be applied
#in the order that we've called them'

def split_string(function):
    def wrapper():
        func =function()
        splitted_string =func.split()
        return splitted_string
    return wrapper

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@split_string #it is a decorator
@uppercase_decorator
def say_hi():
    return 'hello there'
say_hi()

##############################################
#calculating square and cube using decorartors

import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result = func(*args,**kwargs)
        end=time.time()
        total_time=(end-start)*1000
        print(func.__name__+f" took {total_time}mil sec")
        return result
    return wrapper

@time_it
def calc_square(numbers):
    result =[]
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result =[]
    for number in numbers:
        result.append(number*number*number)
    return result

array=range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)

##########################################






    

    
       
        
        
        
        
        