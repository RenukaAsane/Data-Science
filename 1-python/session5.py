# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 08:13:48 2024

@author: Admin
"""
##########################################
car = {
       "brand":"Ford",
       "model":"Mustang",
       "year":1964
       }
x=car.keys()
print(x)
car["color"]="white"
print(car)
x=car.keys()
print(x)

###############################
#removing dict elemnts
car = {
       "brand":"Ford",
       "model":"Mustang",
       "year":1964
       }
car.pop("model")
print(car)

################################
#Acessing keys in dict
for x in car:
    print(x)
###################################
#acessing values
for x in car:
    print(car[x])

########################################
# if u want to access both key and values

for key, value in car.items():
    print("%s == %s" % (key, value))
    
#######################################
#coping dictionary
car = {
       "brand":"Ford",
       "model":"Mustang",
       "year":1964
       }
car2=car.copy()
print(car2)

##########################3
#another way to copy dictionary
thisdict = {
       "brand":"Ford",
       "model":"Mustang",
       "year":1964
       }
dict1=dict(thisdict)
dict1

###################################
#A dictionary can contain dictionaries
#this is called nested dictionaries
our_family={
    "child1":{
        "Name":"Renuka",
        "DOB":"10-05-2003"
        },
    "child2":{
        "Name":"Ashirwad",
        "DOB":"11-01-2008"
        }
    }
our_family
#######################################
#Dictionary method
#clear():to remove all the elements from the car
car = {
       "brand":"Ford",
       "model":"Mustang",
       "year":1964
       }
car.clear()
car

##########################################
#fromkey()
#Create a dictionary with 3 keys, all with
x={'key','key2','key3'}
y=0
thisdict=dict.fromkeys(x,y)
thisdict

##################################
#get():to get the value of dictionary
car = {
       "brand":"Ford",
       "model":"Mustang",
       "year":1964
       }
car.get("model")

#######################################
#item() :returns the dictionarys key-value
car = {
       "brand":"Ford",
       "model":"Mustang",
       "year":1964
       }
car.items()

###########################################
#values():display all th e values of dict
car = {
       "brand":"Ford",
       "model":"Mustang",
       "year":1964
       }
car.values()

#####################################
#update():Insert an item to the dictionary
car = {
       "brand":"Ford",
       "model":"Mustang",
       "year":1964
       }
car.update({"color":"white"})
car

########################################
#for loop
fruits=["Apple","Banana","Orange"]
for i in fruits:
    print(i)

################################
#use of break smt
fruits=["Apple","Banana","Orange"]
for i in fruits:
    print(i)
    if(i=="Banana"):
        break

##########################################
fruits=["Apple","Banana","Orange"]
for i in fruits:
    if i=="Banana":
        break
    print(i)
    
#############################
#continue
fruits=["Apple","Banana","Cherry"]
for x in fruits:
    if x=="Banana":
        continue
    print(x)
    #initially it will take x=0
    #which is apple checks the condition

####################################
#range function
for x in range(2,6):
    print(x)

###################################
for x in range(2,30,3):
    print(x)

##################################
#nested loop is loop inside loop
#the inner loop will be executed one time
colors=["green","yellow","red"]
fruits=["guava","banana","apple"]
for x in colors:
    for y in fruits:
        print(x,y)
        
#####################################
def my_function():
    print("this is me")
my_function()      
########################################
def my_function(name):
    print("Hello" +name)
my_function ("Renuka")

###########################
#positional argument
def my_function(name1,name2):
    print(name1+ " "+name2)
my_function("Renuka","Asane")

def my_function(name1,name2):
    print(name2+ " "+name1)
my_function("Renuka","Asane")

#######################################
#Arbitary Arguments, *args
#if u do not know how many arguments that 
#will be pased into ur fun,
#the fun defination
def my_function(*kids):
    print(kids[0]+" "+kids[2])

my_function("Hello","world","India")

##################################
#kwargs

def myFun(**kwargs):
    for key,value in kwargs.items():
        print("%s == %s" % (key, value))
        
myFun(first='Renuka',mid='Babasaheb',last='Asane')

############################################
#the following example shows how to use default parameter
#if we call the fun without argument it 
#it uses the default value
def my_function(country = "Norway"):
    print("I am from " + country)
    
my_function("Swedan")
my_function("India")
my_function()
my_function("Brazil")

########################################
#passing list as a agrument
#u can send a datatype of argument to a fun

fruits=["orange","banana","guava"]
def my_function(fruits):
    for x in fruits:
        print(x)
my_function(fruits)

############################################
#return value
#to get a function return a value, use th return statment

def my_function(x):
    return x*5
my_function(5)

##########################
#pass function
#havinf an empty fn defination will show
#error without pass
def my_fun():
    pass

##########################
#factorial of a number
#this fun is also called recursive function
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
factorial(3)
factorial(6)

#######################################
# A lambada function is a small
#this fun takes any no of arguments
# but only 1 expression
def add(a):
    sum=a+10
    return sum

add(20)
#using lambda
add=lambda a:a+10
print(add(20))

#lambda fun with any no of arguments
add=lambda a,b:a+b
print(add(5,6))

####################################
#finding odd no from the list
lst=[34,12,64,55,75,13,63]
odd_lst=list(filter(lambda x:(x%2!=0),lst))
print(odd_lst)
#filter:() method accept 2 arguments in python
#a fun and iterable  such as list here iterable is filter

#finding even no from the list
lst=[34,12,64,55,75,13,63]
odd_lst=list(filter(lambda x:(x%2==0),lst))
print(odd_lst)

################################
#assignment(Homework)
#without lambda
lst=[1,2,3,4,5,6,7,8,9,11]
for i in lst:
    i=i**2
    print(i)
#square of numbers enter in the list
#using lambda function
lst = [1, 2, 3, 4, 5,6,7,8,9,10]
sqr = list(map(lambda x: x**2, lst))
print(sqr)
#here map() applies the lambda function
# to each element in lst.
#list() converts the result
# of the map() function into a list.
############################################
#using power function
lst = [1, 2, 3, 4, 5,6,7,8,9,10]
sqr = list(map(lambda x:pow(x, 2), lst))
print(sqr)

######################################












       