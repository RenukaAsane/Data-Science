# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 20:31:48 2024

@author: Admin
"""
#typecasting
#input in the string format
#concatination
 
age = input('Please enter your age:')
print(type(age))
print(age)

age1 = input('Please enter your age:')
print(type(age1))
print(age1)

age2 = input('Please enter your age:')
print(type(age2))
print(age2)

age=age1+age2
print(age)
##############################

#typecasting
age1 = int(input('Please enter your age:'))
print(type(age1))
print(age1)

age2 = int(input('Please enter your age:'))
print(type(age2))
print(age2)

age=age1+age2
print(age)

#####################################

#floting point no
#string to float
exchange_rate =1.83
print(exchange_rate)
print(type(exchange_rate))

################################

#convert to float
#types such as an int or a string into a float
int_value = 100
string_value ='1.5'
float_value = float(int_value)
print('int value as a float:' , float_value)
print(type(float_value))
float_value = float(string_value)
print('string value as a float:',float_value)
print(type(float_value))

######################
#complex number
c1=1
c2=2j
print('c1:', c1, 'c2:',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)
#######################
#Boolean values
#python supports anothe type calls boolean;
#a Boolean type can only be one of true or false

all_ok = True
print(all_ok)
all_ok = False
print(all_ok)
print(type(all_ok))

##############################
#string into boolean
#true or false
status = bool(input('OK it is confirmed?:' ))
print(status)
print(type(status))
############################
#Arithmetic Opetrations
#In python they are represented by one or two character

home=10
away=15
print(home + away)
print(type(home + away))
print(10 * 4)
print(type(10 * 4))
goals_for =10
goals_against =7
print(goals_for - goals_against)
print(type(goals_for - goals_against))
#Division
#in divsion it is converted to float
#using '/' it show type as float
print(10/4)
print(type(10/4))











