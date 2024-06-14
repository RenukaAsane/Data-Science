# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 02:34:50 2024

@author: Admin
"""
#to print odd numbers btwwen range

start,end =4,19
#iterating each num in list
for num in range(start,end +1):
    #checking condition
    if num%2!=0:
        print(num,end =" ")
        
###################################
#to print even numbers btwwen range
start,end =4,19
#iterating each num in list
for num in range(start,end +1):
    #checking condition
    if num%2==0:
        print(num,end =" ")
        
###################################
x,y,z=5,6,7
print(x)
print(y)
print(z)
x,y,z=5 #it wioll show error as only 1 variable get assign num 5
print(x)
print(y)
print(z)

#######################
#global variables
x="awesome"
def my_function():
    print("python is:"+x)
my_function()

#########################
x="awesome"
def my_function():
    x="fantastic"
    print("python is:"+x)
my_function()
#outside of block of code it will print global var otherwise priority is given to local var
print("python is:"+x)

#########################
#getting datatype
x=5
print(type(x))
########################
x=range(6)
print(type(x))

########################
x={"name":"renuka","age":21}
print(type(x))
#######################
str1="hello"
str2=2
str3=str1+str2
#here u will get error:cant conate str and int

################
#string
#if u want multiple strings
x="""This is python.It is very powerful"""
print(x)

##################
#string slicing
#it is use to show any particular value from given text
x="""This is python.It is very powerful"""
print(x[2:8])

###################################
#slice from the start
print(x[:3])

#############
##slicing to the end
print(x[4:])

#negative indexing
print(x[-5:-2])

###################
#modify string
print(x.upper())

####################
x=x.upper()
print(x.lower())

#################
#removing white spaces from 1st to end
x="  This is Python"
print(x.strip())
#lstrip and rstrip
print(x.lstrip())
print(x.rstrip())


####################
x="Hello Renuka"
print(x.replace("Hello","Welcome"))

#############################
#use of split which replace white space/or ,
x="Hello World"
print(x.split(" "))
############################
x="Hello World"
string1=x[::-2]
print(string1) 
################
x="Hello World"
string1=x[::-1]
print(string1) 

############################
#find methods,searches the string for specified value
x="This is python and it is very powerfull"
print(x.find("and"))

######################
#string concateness
x="hello"
y="word"
print(x+y)

#########################
#to add white spaces
print(x+" "+y)

###################
x=21
y="my name is renuka"
print(x+y)
#it will show error as int and string not suported
print(f"my name is renuka and my age is {x}")
###########################
quantity=3
item_no=54
price=67
print(f"I want {quantity} pieces and item number is {item_no} its price is {price}")

#################################
#another method to conatenate string and int
my_order="I want {} pieces and item number is {} its price is {}"
print(my_order.format(quantity,item_no,price))
#########################
#another method to conatenate string and int using id
my_order="I want {0} pieces and item number is {1} its price is {2}"
print(my_order.format(quantity,item_no,price))

#################################
#the escape character allows u to use double quotes when
text="This is fun fair and it has got big \"round rigo \""
print(text)

###############################
#Operator precedence
print(3*3+3/3-3)
"""
Rule for mathematical operations
PEMDAS
P:paranthesis
E:Exponential
M:Multiplication
D:Division
A:Adition
S:Subtraction

"""
####################
#identity opearator
a=2
b=3
print(a is b)
print(a is not b)

#########################
#python list
lst=["cherry","bannana","apple"]
print(lst)
############################
#list items are indexed,1st index has 0
print(lst[0])
print(lst[2])
############################
#append() adds an element at end of list
lst=["cherry","bannana","apple"]
lst.append("Mangao")
print(lst)

#############################
#clear removes all the emt from list
lst=["cherry","bannana","apple"]
lst.clear()
print(lst)
############################
#copy() method
lst=["cherry","bannana","apple"]
lst2=lst.copy()
print(lst2)
#####################################

#count() returns no of items value "cherry"
lst=["cherry","cherry","apple"]
lst.count("cherry")

#################################
#extend() add the elements of cars to the fruits
lst=[1,2,3]
lst1=[4,5,6]
lst.extend(lst1)
print(lst)

###########################
lst=["cherry","cherry","banana"]
lst.insert(1,"Mangao")
print(lst)

############################
lst=["cherry","cherry","banana"]
lst.pop(1)
print(lst)

##################
#remove item with specifed index
lst=["cherry","cherry","banana"]
lst.remove("cherry")
print(lst)

######################
lst=["cherry","cherry","banana"]
lst.reverse()
print(lst)

#########################
#sort() list in alphabetically
lst=["cherry","orange","banana"]
lst.sort()
print(lst)

###############################################
#tuple operations

tup=("cherry","cherry","banana")
print(tup)
print(tup[2])

##############################
#once tuple is created it cant be changed
x=("apple","banana","cherry")
x[1]="kivi"
#it gives error
#first convert it into list
y=list(x)
y[1]="kivi"
#convert list to tuple
x=tuple(y)
print(x)

#########################3
#you can  access tuple item by refering index
print(x[1]) 

#########################
#to join 2 or more tuples u can use + operator
tuple1 = ("a","b","c")
tuple2=(1,2,3)
tup1=tuple1+tuple2
print(tup1)

####################################
#dictionary
dict1={"Brand":"Maruti","model":"2456","year":2011}
print(dict1)
print(len(dict1))
print(type(dict1))

###########################
dict1={
       "Brand":["Maruti","Mahendra","Toyoto"],
       "Model":["a","b","c"],
       "Year":[2011,2012,2013]}
print(dict1)
print(len(dict1))
print(type(dict1))

#######################
#get= to get particular key
dict1.get("Model")
#to get all keys
dict1.keys()





































































    
    

        
        
        
        









        