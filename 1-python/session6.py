# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 08:10:03 2024

@author: Admin
"""
'''
write python code using logical operators and if elif
so as to check height as well as
so as to allow for roller coster also ask user age and 
charge ticket accodingly
'''
#mycode try
print("Welcome to the roller coaster")
height=int(input("please enter your heignt in cm"))
if height >=120:
    print("You are eligible for roller coaster")
    age=int(input("Enter your age in year"))
    bill=0
    if age<12:
        print("child's ticket is 5$")
        bill=5
    elif age>12 and age<18:
        print("your ticket is 25$")
        bill=25
    elif age >18:
        print("your ticket is 50$")
        bill=50
        a=str(input("do u want popcone"))
        if a=='y':
            bill+=3
            print(f"your bill is: {bill}")
        else:
            print(f"your bill is:{bill}")
else :
    print("no entry")
###########

#sirs code

print("Welcome to the roller coaster")
height=int(input("please enter your heignt in cm"))
if height >=120:
    print("You are eligible for roller coaster")
    age=int(input("Enter your age in year"))
    bill=0
    if age<12:
        print("child's ticket is 5$")
        bill=5
    elif age>12 and age<18:
        print("your ticket is 25$")
        bill=25
    elif age >= 18 and age <45:
        print("young ticket is 12$")
        bill=12
    elif age>=45 and age <=55:
        print("Adults ticket is 50 $")
        bill=50
    want_photo=input("Do u want photo Y or  N")
    if want_photo=='Y':
        bill+=3
        print(f"u need to pay {bill} in $")
    else:
        print(f"u need to pay {bill} in $")
        
else:
    print("you are eligible")
    
###########################################################
#BMI(Body Mass Index) Calculator Program

height=float(input("enter ur height in m:"))
weight=float(input("enter ur weight in kg"))
BMI=round((weight/(height*height)),2)
if BMI<18.5:
    print(f"You are under weight and your BMI is:{BMI}")
elif BMI>18.5 and BMI<25:
    print(f"You are under weight and your BMI is:{BMI}")
elif BMI>25 and BMI<30:
    print(f"You are under weight and your BMI is:{BMI}")
elif BMI>30 and BMI<35:
    print(f"You are under weight and your BMI is:{BMI}")
elif BMI>35:
    print(f"you are clinically obese and your BMI is:{BMI}")

############################################################
#write a program to find out is duplicate elements from list 
#used for sorted list
lst1=[1,2,3,4,5,2]
lst1.sort()
#if used sot he returns true

def is_duplicate(lst1):
    for i in range(len(lst1)-1):
        #compare current number with next number
        if(lst1[i]==lst1[i+1]):
            return True
    return False

print(is_duplicate(lst1))

###############################################
#leap year =366 days if not leap year 365 days


def is_leap_year(year):
    if((year>0) and (year%4==0) and (year%100!=0) or (year%400==0)):
        return True
    return False
print(is_leap_year(2000))
print(is_leap_year(2024))
print(is_leap_year(1900))

###############################################
#Write a program to dispay mario pyramid

for i in range(4):
    for j in range(4):
        print("#",end=" ")
    print()

for i in range(4):
    for j in range(i+1):
        print("#",end=" ")
    print()

for i in range(4):
    for j in range(4-i):
        print("#",end=" ")
    print()

##############################
# to print in diamond
def print_diamond(rows):
    # Upper half of the diamond
    for i in range(1, rows + 1):
        # Print spaces
        for j in range(1, rows - i + 1):
            print(" ", end="")
        
        # Print stars
        for k in range(1, 2 * i):
            print("*", end="")
        
        print()

    # Lower half of the diamond
    for i in range(rows - 1, 0, -1):
        # Print spaces
        for j in range(1, rows - i + 1):
            print(" ", end="")
        
        # Print stars
        for k in range(1, 2 * i):
            print("*", end="")
        
        print()


rows = int(input("Enter the number of rows: "))
print_diamond(rows)

    
#####################################
#Minimum and maximum in list

lst=[23,45,2,1,5,7,8,12]
def min_max(lst):
    min=lst[0]
    for i in lst:
        if i<min:
            min=i
    print("The minimum value",min)
    
    max=lst[0]
    for i in lst:
        if i>max:
            max=i
    print("Maximun value",max)

print(min_max(lst))

##########################################
#write a prongram to fing sentence is palindrom or not

def is_palindrome(input):
    if input=="":
        return "You entered wrong input"
    else:
        string=input[::-1]
        if string==input:
            return True
    return False

print(is_palindrome("step on no pets"))

###################################

users=['admin','manager','employee','worker']
for user in users:
    if user=='admin':
        print("Hello this is admin,would u like to see a status report")
    elif user=='manager':
        print("hello this is manager")
    elif user=='employee':
        print("Hello this is employee")
    elif user=='worker':
        print("Hello this is worker ")
    else:
        print("Hello")

#######################################
#enter the role by user
user=str(input("Enter the role:"))
if user=="admin":
    print("hello admin")
elif user=="employee":
    print("hello amoloyee")
elif user=="manager":
    print("hello manager")
else:
    print("hello")

######################################
#password picker
print("Welcome to password picker")
#pick the adjective
adjectives=['sleepy','slow','smelly','wet','fat','red','orange','yellow','green','blue','purple','fluffy','white','proud','brave']
#pick the nouns
nouns=['apple','dinosaur','ball','toaster','goat','dragon','hammer','dunk','panda']
#pick the words
import random
import string

adjective=random.choice(adjectives)
noun= random.choice(nouns)
#select the number
number=random.randrange(0,100)
#select a special character
special_char = random.choice(string.punctuation)
#create new secure password
password = adjective +noun + str(number) + special_char
print("your new password is: %s:" %password)

################################################
#input from user
import random
import string
while True:
    adjective=random.choice(adjectives)
    noun= random.choice(nouns)
    #select the number
    number=random.randrange(0,100)
    
    special_char = random.choice(string.punctuation)
    
    password = adjective +noun + str(number) + special_char
    print("your new password is: %s:" %password)
    response=input("Would u like to generate another password?")
    if response =='n':
        break
    







        
        
    


    



        
        
        
        
        
        
        
        
        
        