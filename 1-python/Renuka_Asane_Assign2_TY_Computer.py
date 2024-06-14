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

#######################################################################

'''
2. Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message.

'''
def find_shape(side):
    if side == 3:
        return "It is triangle"
    elif side == 4:
        return "It is quadrilateral"
    elif side == 5:
        return "It is pentagon"
    elif side == 6:
        return "It is hexagon"
    elif side == 7:
        return "It is heptagon"
    elif side == 8:
        return "It is octagon"
    elif side == 9:
        return "It is nonagon"
    elif side == 10:
        return "It is decagon"
    else:
        return "shape with this number of sides not exist"

side = int(input("Please enter the number of sides: "))
print(f"The shape: {find_shape(side)}.")

#################################################################################################

'''
3.The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed.
'''
name = input('Enter the month :  ')

thirty_days = ['April','June','September','November']
thirty_one_days = ['January','March','July','August','October','December']
feb = ['February']

if name in thirty_days:
    print('Number of days: 30')
elif name in thirty_one_days:
    print('Number of days: 31')
elif name in feb:
    print('Number of days: 28 or 29')
else:
    print("Invalid input ")

###########################################################################
'''
4. A triangle can be classified based on the lengths of its sides as equilateral, isosceles
or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the user.
Display a message indicating the type of the triangle.
'''
print("Input lengths of the triangle sides: ")
side1 = int(input("Enter the side 1: "))
side2 = int(input("Enter the side 2: "))
side3 = int(input("Enter the side 3: "))
 
if side1 == side2 == side3:
    print("Triangle is Equilateral triangle")
elif side1==side2 or side2==side3 or side3==side1:
    print("Triangle is Isosceles triangle")
else:
    print("Triangle is Scalene triangle")
    
###########################################################
'''
5.The year is divided into three seasons: summer, rainy 
and winter.While the exact dates that the seasons 
change vary a little bit from year to year because of the
way that the calendar is constructed, Write a program to 
display the season if date is given.
'''
def know_season(month, day):
    if (month == "March") or (month == "April") or (month == "May" ) or (month =="June"): 
        return "Summer"
    elif (month == "July") or (month == "August") or (month == "September") or (month == "October"):
        return "Rainy"
    else:
        return "Winter"

def main():
    month = input("Enter the month  : ")
    day = int(input("Enter the day :"))

    season = know_season(month, day)
    print (month,day,"is in :",season)
main()

######################################################################















    