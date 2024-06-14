# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 08:44:38 2024

@author: Admin
"""
################################################
'''we should know pandas 70%,numpy 20% and matplotlib 10%'''
'''Matplotlib'''
#########################################
'''df.describe()
1.mean
2.max
3.Min
4.std deviation
5.Q1
  Q2
  Q3
  '''

#################################33
'''matplotlib and seaborn are same only 
differnce is that seaborn has more interactive GUI'''

#######################################3
'''Bar Graph'''
#Write a Python to draw a line with sutiable label
import matplotlib.pyplot as plt
X=range(1,50)
Y = [value *3 for value in X]
print("Value of X :")
print(*range(1,50))

'''
This is equivalent to (mario pyramid)
i in range (1,50):
    print(i,end=" ")
'''

print("Values of Y(thrice of X):")
print(Y)

################################
'''execute this code at a time'''
#plot lines and markers to Axes
plt.plot(X,Y)
#set the x axis label of the current axis
plt.xlabel('x-axis')
#set the y axis label of the current axis
plt.ylabel('y-axis')
#set title 
plt.title('Draw the line')
#Display the figure
plt.show()#there is no need to execute this line of code just it is a part of code
 
#####################################
#label in the x - axis, y- axis and a title 
import matplotlib.pyplot as plt
#x axis values
x = [1,2,3]
#y axis values
y = [2,4,1]
#Plot lines and/or markers to the Axes
plt.plot(X,Y)
#Set the x- axis label of the current axis
plt.xlabel('x-axis')
#Set the y- axis label of the current axis
plt.ylabel('y-axis')
#set a title 
plt.title('Sample Graph')
#display figure
plt.show()

##############################################3
##############################################3
#Write a Python Program to plot two or more lines
#on same plot with suitable legends of each line
import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,10]

#line 2 points
x2=[10,20,30]
y2=[40,10,30]

#plotting the line 1 points
plt.plot(x1,y1,label ="line 1")
#ploting the line 2 points
plt.plot(x2,y2,label="line 2")
#set the x-axis label of the current axis
plt.xlabel('x-axis')
#set the y-axis label of the current axis
plt.ylabel('y-axis')
#set a title of the current axes
plt.title("Two or more lines on some plot with suitable legend")
#show the legend on the plot
plt.legend()
#Display a figure 
plt.show()

##############################################
#Write a Python Program to plot two or more lines
#
import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,10]

#line 2 points
x2=[10,20,30]
y2=[40,10,30]

#set the x-axis label of the current axis
plt.xlabel('x-axis')
#set the y-axis label of the current axis
plt.ylabel('y-axis')
#set a title 
plt.title("Two or more lines with different widths and colours with:")
#Display a figure 
plt.plot(x1,y1, color='blue' , linewidth = 3 ,label='line1')
plt.plot(x2,y2, color='red' , linewidth = 5 ,label='line2')
plt.legend()
plt.show() 

#################################################
#write  a python program to draw two or more lines with different style 
import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,10]

#line 2 points
x2=[10,20,30]
y2=[40,10,30]

#set the x-axis label of the current axis
plt.xlabel('x-axis')
#set the y-axis label of the current axis
plt.ylabel('y-axis')
#set a title 
plt.title("Two or more lines with different widths and colours with:")
#Display a figure 
plt.plot(x1,y1, color='blue' , linewidth = 3 ,label='line1-dotted',linestyle='dotted')
plt.plot(x2,y2, color='red' , linewidth = 5 ,label='line2-dotted',linestyle='dashed')
plt.legend()
plt.show()  

########################################
#write  a python program to draw two or more lines
#and set the line markkers
import matplotlib.pyplot as plt
#x axis values
x = [1,4,5,6,7]
#y axis values
y = [2,6,3,6,3]

#ploting the points
plt.plot(x,y, color='red',linestyle='dashdot',linewidth = 3,
         marker='o', markerfacecolor='blue',markersize=12)
#Set the y-limits of the current axes
plt.ylim(1,8)
#Set the x-limits of the current axes
plt.xlim(1,8)
#naming the x- axis
plt.xlabel('x-axis')
#naming the y- axis
plt.ylabel('y-axis')

#giving the title to my graph
plt.title('Display Markrer')
#function to show th plot
plt.show()

#######################################################3
'''Write this code in quick reference pages'''
#Write a python programming to display a verticular
#a bar chart of the popularity of programming Languages
import matplotlib.pyplot as plt
x = ['Java','Python','PHP','JavaScript','C#','C++']
popularity =[22.2,17.6,8.8,8,7.7,6.7]
x_pos =[i for i, _ in enumerate(x)]#list comprehension
plt.bar(x_pos,popularity,color='hotpink')
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title("Popularity of programming langauge\n"+"Worldwide,Oct 2017 compared to a year ago")
plt.xticks(x_pos,x)
#Turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='black')
plt.show()

######################################################

#Write a python programming to display a horizontal
#a bar chart of the popularity of programming Languages
import matplotlib.pyplot as plt
x = ['Java','Python','PHP','JavaScript','C#','C++']
popularity =[22.2,17.6,8.8,8,7.7,6.7]
x_pos =[i for i, _ in enumerate(x)]#list comprehension
plt.barh(x_pos,popularity,color='green')#in horizontal give 'barh'
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title("Popularity of programming langauge\n"+"Worldwide,Oct 2017 compared to a year ago")
plt.yticks(x_pos,x)#here give yticks for horizontal graph
#Turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='black')
plt.show()

########################################################
#Write a python programming to display a
#a bar chart of the popularity of programming Languages
#Use uniform color
import matplotlib.pyplot as plt
x = ['Java','Python','PHP','JavaScript','C#','C++']
popularity =[22.2,17.6,8.8,8,7.7,6.7]
x_pos =[i for i, _ in enumerate(x)]#list comprehension
plt.bar(x_pos,popularity,)
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title("Popularity of programming langauge\n"+"Worldwide,Oct 2017 compared to a year ago")
plt.xticks(x_pos,x)
#Turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='black')
plt.show()

###################################################
#colour for the graph
import matplotlib.pyplot as plt
x = ['Java','Python','PHP','JavaScript','C#','C++']
popularity =[22.2,17.6,8.8,8,7.7,6.7]
x_pos =[i for i, _ in enumerate(x)]#list comprehension
plt.bar(x_pos,popularity,color=['red','orange','blue','pink','green','yellow'])
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title("Popularity of programming langauge\n"+"Worldwide,Oct 2017 compared to a year ago")
plt.xticks(x_pos,x)
#Turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='black')
plt.show()

##################################################






