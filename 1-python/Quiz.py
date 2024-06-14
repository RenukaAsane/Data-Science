# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 08:20:16 2024

@author: Admin
"""


#12.Find the output of the code given below?
lst= [ int(x/3) for x in range(5,35) 
      if x % 2 == 0 and x%5 == 0]
print(lst[-1]+5)

#13.What would be the output of the following code snippet?
Func1=lambda x: ((x + 3) * 5 / 2)

Func1(3)

#############################################
#1.What is the output of this code?
def foo(a, b=4, c=6):
    print(a, b, c)
foo(20, c=12)

#o/p 20 4 12

###############################

#2.Write   code  which will give you "Apples"?
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries","Pears"]
#Ans:-
print(fruits[2])

##################################
#3.Given the code below:
#What do you think will be printed?
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)

#Ans:-
'''
['Strawberries', 'Nectarines', 'Apples', 
       'Grapes', 'Peaches', 'Cherries', 
       'Melons', 'Lemons']
'''

########################################
#4.Write a line of code will change the 
#starting_dictionary to the final_dictionary?
starting_dictionary = {
"a": 9,
"b": 8,
}
final_dictionary = {
"a": 9,
"b": 8,
"c": 7,
}

#Ans:-
starting_dictionary=final_dictionary.copy()
print(starting_dictionary)
#And o/p :- {'a': 9, 'b': 8, 'c': 7}

#############################################
#Which line of code will print "Steak"?
order = {
	    "starter": {1: "Salad", 2: "Soup"},
	    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
	    "dessert": {1: ["Ice Cream"], 2: []},
	}

#Ans:-  
print(order["main"][2][0])

##############################################
#6.Without running the code below, what do you think will be printed in the console? 
def add(n1, n2):
	  return n1 + n2
  
def subtract(n1, n2):
      return n1 - n2
  
def multiply(n1, n2):
      return n1 * n2
 
def divide(n1, n2):
	  return n1 / n2

print(add(2, multiply(5, divide(8, 4))))

#Ans:- 12

#####################################################
#7.What would you predict to be the result of running the following code?
def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
	 
result = outer_function(5, 10)
print(result)

#Ans:-15

#########################################################
#8. Select the correct ways to get the value of marks key.
student = {
  "name": "Emma",
  "class": 9,
  "marks": 75
}

#Ans:-
student.get("marks")

########################################################
#10.Suppoes you have dict1 and dict2,write  way to copy
# a dictionary in Python
dict1={1:'Python',2:'DataScience',3:'NLP'}
dict2={4:'list',5:'Tuple',6:'Dict'}

dict1=dict2.copy()
dict1

#########################################################
#11.Find the output of the code given below?
lst = [int(x*x) for x in range(3,12,4)]
print(lst[-2])

#Ans: 49
#because x*x is in gap of 4 i.e 3,7,11 and on -12 it is 7 so 49

###########################################################
#12.Find the output of the code given below?
lst= [ int(x/3) for x in range(5,35) if x % 2 == 0 and x%5 == 0]
print(lst[-1]+5)

#Ans:- 15

###############################################################
#13.What would be the output of the following code snippet?
Func1=lambda x: ((x + 3) * 5 / 2)

Func1(3)

#Ans:- 15.0











