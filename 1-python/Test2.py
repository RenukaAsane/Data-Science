# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 08:20:48 2024

@author: Admin
"""

##############################################
'''Que -1 :-1.Write a Python function that 
takes two lists and returns True if they 
have at least one common member
'''
def common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False
list1 = [1, 2, 3, 4, 5]
list2 = [10, 6, 1, 8, 9]
print(common_member(list1, list2))

###########################################

'''2. Use list comprehension to construct
a new list but add 6 to each item.'''
#Ans:-

ori_lst = [1, 2, 3, 4, 5]
new_list = [x + 6 for x in ori_lst]
print(new_list)

###########################################

'''3.Write a Python program to reverse a 
string.'''
#Ans:-

r1=input("Enter the string: ")
str1 =r1 [::-1]
print(str1)

##########################################
'''4. Write a Python program to iterate over
dictionaries using for loops.'''
#Ans :-


#############################################
'''5. Using dict comprehension and a 
conditional argument create a dictionary 
from the current dictionary where only the 
key:value pairs with value above 2000 are 
taken to the new dictionary.'''
#Ans:-
# Current dictionary
current_dict = {'A': 1500, 'B': 2500, 'C': 1800, 'D': 3000}

# New dictionary with key-value pairs where value > 2000
new_dict = {key: value for key, value in current_dict.items() if value > 2000}

# Output the new dictionary
print(new_dict)


#############################################
'''6.Open the file data.txt using file 
operations.'''
#Ans:-



##########################################
'''7. Define a array ,
data = array([11, 22, 33, 44, 55]) 
find 0 th index 4 th index dat'''
#Ans:-
array= ([11, 22, 33, 44, 55])
array[0]
array[4]


############################################
'''8. Write a Python program to filter a
list of integers using Lambda. 
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
#Ans:-
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using lambda function to filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, original_list))
even_numbers

#Using lambda function to filter odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, original_list))
odd_numbers

##############################################
'''9. Write a Pandas program to create the specified columns
and rows from a given data frame.
name': ['Anna', 'Dinu', Ramu', 'Ganu', 'Emily', 'Mahesh', 'Jayesh', ‘venkat', 'Ajay', 'Dhanesh']
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19]
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']'''
#Ans:-

import pandas as pd
import numpy as np
stud=({
       'name': ['Anna', 'Dinu', 'Ramu', 'Ganu', 'Emily', 'Mahesh', 'Jayesh', 'venkat', 'Ajay', 'Dhanesh'],
       'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
       'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
       'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
       'labels' : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
       })
df=pd.DataFrame(stud)
df


###################################################################

'''10. Define a array data = array([11, 22, 33, 44, 55]) 
and slice it from 1 to 4'''
#Ans:-

data = np.array([11, 22, 33, 44, 55])
x=data[1:4]
print(x)

#################################################################
 


