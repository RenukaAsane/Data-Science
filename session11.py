# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 08:16:16 2024

@author: Admin
"""
'''OOPS Concepts...Classes and Objects in Python'''
#tom is reference or handler for the object

class Human:
    def __init__(self,n,o):#constructor
        self.name=n
        self.occupation=o
        
    def do_work(self):
        if self.occupation =="tennis player":
            print(self.name, "plays tennis")
        elif self.occupation == "actor":
            print(self.name, "shoots films")
    
    def speaks(self):
        print(self.name, "says how are you?")

tom = Human("tom_cruise","actor")
tom.do_work()
tom.speaks()

####################################################
'''Inheritance'''
#single inheritance
class vehicle:
    def general_usage(self):
        print("general use:transportation")

class car(vehicle):
    def __init__(self):
        print("I am car")
        self.wheels = 4
        self.has_roof = True
    
    def specific_usage(self):
        self.general_usage()
        print("specific use: commute to work,vacation with family")

class MotorCycle(vehicle):
    def __init__(self):
        print("I'am motor cycle")#this is written in constructor
        self.wheels = 2
        self.has_roof = False
    
    def specific_usage(self):
        self.general_usage()
        print("specific use: local communication,racing")

c=car()
m=MotorCycle()
c.specific_usage()
m.specific_usage()
print(issubclass(car,MotorCycle))#o/p-False
print(issubclass(car,vehicle))#o/p-True
#here next argument should be parent class of 1st argument

####################################################
#multiple inheritance
class Father():
    def skills(self):#this is not constructor
        print("I like gardening,programming")

class Mother():
    def skills(self):
        print("I like cooking,art")

class Child(Father,Mother):
    def skills(self):
        Father.skills(self)#method of base class with Father reference
        Mother.skills(self)#method of base class with Mother reference
        #here as Mother and Father class have same function
        print("I like sports")
        
c=Child()
c.skills()

########################################################

        





