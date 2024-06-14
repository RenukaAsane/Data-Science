# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 08:18:42 2024

@author: Admin
"""
##################################################
'''multiple except block
Sometimes , a single peice of code might
be suspected to have more than 1 type of error.
For handling such exception multiple exceptions
are used '''
try:
    numerator=50
    denom=int(input("Enter the denominator:"))
    quotient=(numerator/denom)
    print("Division performed sucessfully")
except ZeroDivisionError:
    print("Denominator as ZERO is not allowed")
except ValueError:
    print("Only INTEGERS should be entered")

#################################################
#Handling exception without naming
#(unknown exception)

try:
    numerator=50
    denom=int(input("Enter the denominator:"))
    quotient=(numerator/denom)
    print("Division performed sucessfully")
except ValueError:
    print("Only INTEGERS should be entered")
except:
    print("OOPS......SOME EXCEPTION RAISED")

##############################################
#Handling exception using "try....except...else"
#error in this code
try:
    numerator=50
    denom=int(input("Enter the denominator"))
    quotient(numerator/denom)
    print("Devision performed sucessfully")
except ZeroDivisionError:
    print("Denominator as ZERO is not allowed")
except ValueError:
    print("Only INTEGERS should be entered")
else:
    print("Result of Division operation is:",quotient)
    
####
try:
    numerator=50
    denom=int(input("Enter the denominator:"))
    quotient=(numerator/denom)
    print("Division performed sucessfully")
except ZeroDivisionError:
    print("Denominator as ZERO is not allowed")
except ValueError:
    print("Only INTEGERS should be entered")
else:
    print("Result of Division operation is:",quotient)

###################################################
#Handling exception using  "try....except...else...finally"
try:
    numerator=50
    denom=int(input("Enter the denominator:"))
    quotient=(numerator/denom)
    print("Division performed sucessfully")
except ZeroDivisionError:
    print("Denominator as ZERO is not allowed")
except ValueError:
    print("Only INTEGERS should be entered")
else:
    print("Result of Division operation is:",quotient)
finally:
    print("OVER AND OUT")

###################################################







 