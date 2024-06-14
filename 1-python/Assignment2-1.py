# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 20:10:54 2024

@author: Admin
"""
'''
1.Write a program that reads a letter of the
 alphabet from the user. If the user enters
 a, e, i, o or u then your program should display
 a message indicating that the entered letter is 
 a vowel. If the user enters y then your program
should display a message indicating that sometimes
 y is a vowel, and sometimes y is a consonant. 
 Otherwise your program should display a message
indicating that the letter is a consonant.

'''
vowels=['a','e','i','o','u']
let=str(input("Enter the letter u want to check :"))
if let in vowels:
    print("Letter is vowel")
elif let == "y":
    print("Sometimes 'y' is vowel sometimes it is constant")
else:
    print("Letter is constant")
    
##############################################################################################################################

'''
2. Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message.

'''
sides = int(input("Please enter the  number of sides : "))
def find_shape(sides):
        
    if sides == 3:
        return "triangle"
    elif sides == 4:
        return "quadrilateral"
    elif sides == 5:
        return "pentagon"
    elif sides == 6:
        return "hexagon"
    elif sides == 7:
        return "heptagon"
    elif sides == 8:
        return "octagon"
    elif sides == 9:
        return "nonagon"
    elif sides == 10:
        return "decagon"
    
print(f"The shape is {find_shape(sides)}.")
###############################################################################################################################
def find_shape(sides):
    shapes = {3: "triangle", 4: "quadrilateral", 5: "pentagon", 6: "hexagon", 7: "heptagon", 8: "octagon", 9: "nonagon", 10: "decagon"}
    return shapes.get(sides, " with unknown sides")

sides = int(input("Please enter the number of sides: "))
print(f"The shape : {find_shape(sides)}.")

'''
The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed.
'''




    