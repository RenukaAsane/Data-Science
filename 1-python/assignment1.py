# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 21:13:07 2024

@author: Admin

"""
#Exercise 1: Mailing Address
"""
Write a program that displays your name and complete 
mailing address formatted in the manner that you
would usually see it on the outside of an envelope.
Your program does not need to read any 
input from the user.
"""
def address():
    name = "Renuka Asane"
    street_address = "36 Rachana Park"
    city = "Kopargaon"
    state = "Maharashtra"
    postal_code = "423601"
    country = "India"
    
    print(name)
    print(street_address)
    print(f"{city},{state} {postal_code}")
    print(country)
# here address function is called 
# outside the function defination
address()

#############################################################################

#Exercise 2:Area of a Room
"""
Write a program that asks the user to enter the width and length of a room. Once
the values have been read, your program should compute and display the area of the
room. The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with.
"""
# Inputing the length and breadth of the room
width=float(input("Please input Width of Room: "))
length=float(input("Please input Length of Room: "))
area= width *length
print( "The area of the room is : ", area, "square meters")

###########################################################################

#Exercise 3:Area of a Field
"""
Create a program that reads the length and width
of a farmer’s ﬁeld from the user in feet. 
Display the area of the ﬁeld in acres.
Hint: There are 43,560 square feet in an acre.
"""
# Input the length and width of the room
width=float(input("Width of field is: "))
length=float(input("Length of field is: "))
area_farm= width *length/43560
print( "The area of the farm is : ", area_farm, "acres")

#############################################################################

#Exercise 4: Bottle Deposits
"""
In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places.
"""   
def calculate_refund(less, more):
    refund1 = less * 0.10
    refund2 = more * 0.25
    total_refund = refund1 + refund2
    return total_refund
    
def main():
    less = int(input("Enter the number of containers holding one liter or less: "))
    more = int(input("Enter the number of containers holding more than one liter: "))
    
    total_refund = calculate_refund(less, more)

    print("The total refund for returning the containers is : $",total_refund)
main()

##########################################################################

#Exercise 5:Tax and Tip
"""
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.
"""

tax_rate = 0.08  # Assume a tax rate of 8%
tip_rate = 0.18  # Tip rate is 18%
meal_cost = float(input("Enter the cost of the meal: "))
tax_amount=meal_cost * tax_rate
tip_amount=meal_cost * tip_rate

total_cost = meal_cost + tax_amount + tip_amount
print(f"Tax: ${tax_amount:.2f}")
print(f"Tip: ${tip_amount:.2f}")
print(f"Total cost including tax and tip is: ${total_cost:.2f}")

#######################################################################

#Exercise 6:   Height Units
"""
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
"""

feet = int(input("Enter the number of feet: "))
inches = int(input("Enter the number of inches: "))

total_inches = feet * 12 + inches
centimeters = total_inches * 2.54

print(f"The equivalent height is {centimeters:.2f} centimeters.")

#############################################################################














