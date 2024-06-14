# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:16:39 2024

@author: Admin
"""
#if we want o/p in integer type use //
print(100//20)
print(type(100//20))

#But what if you are only interested in the reminder part of a division
#the integer division operator has lost?
#well in the case you can use the modululs operator

print('Modulus division 100 % 13:',100%13)
print('Modulus division 3 % 2:',3%2)

################################
#the power operator is '**'
a=5
b=3
print(a**b)
          
#assignmwent operator
x=0
x
x+=1 #has the same behavioe as x = x+1
x

################################33
#none value
#python has a special type
#the Nonetype,which a sinfle value
winner=None
print(winner is None)
#alternative you can also write:
print(winner is not None)

winner=None
print('winner',winner)
print('winner is none',winner is None)
print('winner is not none',winner is not None)
print(type(winner))

#Comparison operator
#flow of control usinf if statment
num = int(input('Enter a number:'))
if num > 0:
    print(num)
    
#Now lets give intendation
num = int(input('Enter a number: '))
if num > 0:
    print(num)

#########################3

#else in a if statment
num = int(input('Enter yet another number: '))
if num < 0 :
    print('It is Negative')
else:
    print('Its not Negative')

############################
#the use of elif
savings = float(input("Enter how much is ur savings:"))
if savings == 0:
    print("Sorry no savings")
elif savings < 500:
    print("Well done")
elif savings < 1000:
    print("Thats a tidy sum")
elif savings <= 10000:
    print("Welcome sir!")
else:
    print("thankyou!")
    
############################
#Iteration/looping
#while loop

count = 1
print("Starting")
while count <=10:
    print(count)
    count+=1

#############################################
#for loop
#loop over a set of values in a range
print("Print out values in a range")
for i in range(2,10):
    print(i)
    print("done")

############################################
print("Only print code if all iteratrion complete")
num =int(input("Enter a number to check for: "))
for i in range(0,16):
    if i==num:
        break
    print(i)
print('done')
#############################
#Now use an 'anonymous' loop variable
for _ in range(0,10):
    print('.')
    print()
    
for _ in range(0,10):
    print('.', end='')
    print()
    
#########################
#to print dot in horizontal
for _ in range(0,10):
    print('.', end='')



    










