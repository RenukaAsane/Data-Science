# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:14:11 2024

@author: Admin
"""
#####################################################
# 1. Create lower triangular, upper triangular and pyramid 
#containing the "*" character.
######################################################

#Lower Triangular

def lower_tri(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()

n = 5
lower_tri(n)

#######################################################

#Upper Triangular

def upper_tri(n):
    for i in range(n):
        for j in range(n):
            if j >= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

n = 5
upper_tri(n)

#######################################################

#Pyramid

def pyramid(n):
    for i in range(n):
        # To Print spaces
        for j in range(n - i - 1):
            print(" ", end=" ")
        # To Print stars
        for j in range(2 * i + 1):
            print("*", end=" ")
        print()
n = 5
pyramid(n)

######################################################

