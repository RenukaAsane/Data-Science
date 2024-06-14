# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:17:48 2024

@author: Admin
"""
#reduce space complexity
lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)
###############################
#we can write same method using list comprehension

#list Comprehension
lst=[num for num in range(0,20)]
print(lst)

#################################
#it will capalize first letter
names=['renuka','deepti','anushka']
lst=[name.capitalize() for name in names]
print(lst)

##############################
#list comprehension with if statment
#write if statment to the right side of for
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]

print(lst)

################################
#for loop inside for loop using list comprehension
lst=[f"{x}{y}" for x in range(3)for y in range(3)]
print(lst)    
###########################################
#Dictionary Comprehension
dist={x:x*x for x in range(3) }
print(dist)

#####################################
#Generator
#in a simple way
#it uses the keyword "yield"
#instead of returning it in a defined function
#Generators are implemented using the function
gen=(x for x in range(3))
print(gen)
for num in gen:
    print(num)
######################
gen=(x for x in range(3))
next(gen)
next(gen)

########################################
#function which returns multiple values
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)

##########################################
#now instead of using for loop we can write our own
gen=range_even(6)
next(gen)
next(gen)
next(gen)

#####################################
#Chaining Generators(generator inside generator)
'''
ele* appears to be placeholder for an elements
 from an iterable.The asteriic
'''
#measure the string
def lengths(itr):
    for ele in itr:
        yield len(ele)
        
#hide the string
def hide(itr):
    for ele in itr:
        yield ele* '*'
        
passwords=["not-good","give 'm-password","00100=100"]
for password in hide(lengths(passwords)):
    print(password)
    
##################################################
#take the input from the user
#homework
import random
import string
noun=str(input("Enter the noun"))
adjective=str(input("Enter the adjectives"))

number=random.randrange(0,100)
special_char = random.choice(string.punctuation)
passw=(adjective + noun +str(number) + special_char)
print(passw)
for password in hide(lengths(passw)):
    print(password ,end="")

###############################################
#afternoon session
###############################################
#Enumerate
#printing list with index
lst=["milk","Egg","Bread"]
for index in range(len(lst)):
    print(f'{index+1} {lst[index]}')

#using enumerator
lst=["milk","Egg","Bread"]
for index,item in enumerate(lst,start=1):
    print(f'{index} {item}')

##############################################
#use of zip function
name=["dada","mama","kaka"]
info=[9850,6032,9785]
for nm,inf in zip(name,info):
    print(nm,inf)

#######################################
#use of zip function with mis match list
name=["dada","mama","kaka","baba"]
info=[9850,6032,9785]
for nm,inf in zip(name,info):
    print(nm,inf)
    #it will not dispay excess mismatch item in name
    #i.e baba

#########################################
##zip longest
from itertools import zip_longest
name=["dada","mama","kaka","baba"]
info=[9850,6032,9785]
for nm,inf in zip_longest(name,info):
    print(nm,inf)
#######################################
#use of fill value instead None
name=["dada","mama","kaka","baba"]
info=[9850,6032,9785]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)

###########################################
#use of all(),if all the values are true
#then o/p is shown
lst=[2,3,-6,8,9]
##values must be non zero,+ve or -ve
if all(lst):
    print("all values are true")
else:
    print("there are null values")

##########################
lst=[2,3,0,8,9]

if all(lst):
    print("all values are true")
else:
    print("there are null values")

####################################
#use of any if any one non zero value
lst=[0,0,0,-8,0]

if any(lst):
    print("It has some non zero values")
else:
    print("Useless")
#########################3
#use of any
lst=[0,0,0,0,0]

if any(lst):
    print("It has some values")
else:
    print("All values are zero in the list")

###############################################
#count()
#use in image processing
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

##############################################3
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))

#################################################3
#cycle()
#aquire the data in real time mode
#suppose u  have repeated task to be done,then u
import itertools

instructions=("Eat","code","sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)

##########################################################
#repeat()
from itertools import repeat
for msg in repeat("keep patience",times=5):
    print(msg)                                                                                                 

################################################################
##combinations()
#combination is picking bolls from box
#premutation means aranging them
from itertools import combinations
players=["John","Jani","Janardhan"]
for i in combinations(players,2):
    print(i)
#for 5 elements
from itertools import combinations
players=["John","Jani","Jay","Janardhan","Ashirwad"]
for i in combinations(players,2):
    print(i)

######################################################
#Permutations
from itertools import permutations
players=["John","Jani","Janardhan"]
for seat in permutations(players,2):
    print(seat)

##################################################
#product()
from itertools import product
team_a=['Rohit','Pandya','Bumrah']
team_b=['virat','Manish','Sami']
for pair in product(team_a,team_b):
    print(pair)

########################################
age=[27,15,35,77]
adults=filter(lambda age:age>=18,age)
print([age for age in adults])

'''Shallow Copy and Deep Copy'''
'''In python,assignment statment(obj_b=obj_a)
do not create real copies'''
#Assignment operation
#this will only create a new variable with the same reference
list_a=[1,2,3,4,5]
list_b=list_a

list_a[0]=-10
print(list_a)
print(list_b)







    

 
        
        








