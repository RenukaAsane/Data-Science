# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:32:21 2024

@author: Admin
"""
'''Exception Handling'''
#divide by zero is the exception
try:
    numerator=50
    denom=int(input("Enter the denominator:"))
    quotient=(numerator/denom)
    print(quotient)
    print("Division performed sucessfully")
except ZeroDivisionError:
    print("Oh this is divide by zero error...not allowed")
print("OUTSIDE try...except block")

################################################
#multiple except block
try:
    numerator=50
    denom=int(input("Enter the denominator:"))
    quotient=(numerator/denom)
    print("Division performed sucessfully")
except ZeroDivisionError:
    print("Denominator as ZERO is not allowed")
except ValueError:
    print("Only INTEGERS should be entered")

########################################