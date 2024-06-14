# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 08:46:41 2024

@author: Admin
"""

'''NumPy'''
''' Numpy is ued for image processing'''
#It is open sourse python library
#used for scientific computing applications,
#abd it stands for Numerical Python
#which is consit of multidimentional array
# All the elements in a Numpy 
#array should be homogeneous

#Array in Numpy
#Create ndarray
import numpy as np
arr=np.array([10,20,30])
print(arr)

######################
#Create a Multi-Dimentional Array
#Create multi Dimentional array
#All features in dataframe are called dimention
arr = np.array([[10,20,30],[40,50,60]])
print(arr)

###########################3
#[[[ ]]] -> 3 dimentional array
#Minimum dimention
#specify ndmin for minimum dimention
arr = np.array([10,20,30,40],ndmin = 3)
print(arr)
#o/p :- [[[10 20 30 40]]]

########################3
#Change the data type 
#dtype parameter
arr = np.array([10,20,30],dtype = complex)
print(arr)
#o/p :- [10.+0.j 20.+0.j 30.+0.j]

##############################

#Get the dimentions of array
arr = np.array([[1,2,3,4],[7,8,6,8,],[9,10,11,12]])
print(arr.ndim) #o/p- 2
print(arr)
#o/0 :-[[ 1  2  3  4]
#       [ 7  8  6  8]
#       [ 9 10 11 12]]

################################
##Finding the size of each item in the array
arr = np.array([10,20,30])
print("Each item contains in byte:",arr.itemsize)

######################################3
#Get the size and shape of array
arr = np.array([[10,20,30,40],[60,70,80,90]])
print("Array size:",arr.size)
print("Shape :",arr.shape)
#array size is 8 i.e (2*4)
#shape =(2,4)

#########################3
#Creating numpy array from list
#Creation of array
#by defalut it will take int
arr = np.array([10,20,30])
print("Array:",arr)

#################################333
#Creating array from list with type float
#converting into float
arr = np.array([[10,20,30],[30,40,50]] ,dtype='float')
print("Array created by using list: \n",arr)
#o/p :-
'''
Array created by using list: 
 [[10. 20. 30.]
 [30. 40. 50.]]'''
 
###################################################
#Craeting a sequence of integers using arange()
#Cerate a sequence of integes
#from 0 to 20 with steos of 3
arr = np.arange(0,20,3)
print("A sequential array with steps of 3:\n",arr)

#Array indexing in Numpy
#o/p :- [ 0  3  6  9 12 15 18]
########################################
arr = np.arange(11)
arr
'''
o/p :
    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
    '''
print(arr[2])
#o/p:-2

print(arr[5]) #o/p :-5

###########################3
#negitive indexing
print(arr[-2])
#o/p:-9

print(arr[-5])
#o/p:-6

################################3
#Multi dimentional array indexing
#Access multidimentional array element
#using array indexing
arr = np.array([[10,20,30,40,50],[20,30,50,10,30]])
print(arr)
#o/p:-
'''
[[10 20 30 40 50]
 [20 30 50 10 30]]
'''
print(arr.shape)
#0/p :- (2,5) 
#now array is 3 dimentional

print(arr[1,1])
 #o/p  30
 
print(arr[0,4])
#50

print(arr[1,-1])
#30

############################3
#accessing array elemrnt usinfg slicing
arr = np.array([0,1,2,3,4,5,6,7,8,9])

x=arr[1:8:2] #start :end : in step of 2
print(x)
#o/p :-[1 3 5 7]

#########example  -2
x=arr[-2:3:-1] #start last but one (-2) upto 3 but not
print(x)
#o/p :-[8 7 6 5 4]

################ example -3
x= arr[-2:10]
print(x)
#o/p:- 8,9

###################################
#indexing in numpy
multi_arr = np.array([[10,20,10,40],
                      [40,50,70,90],
                      [60,10,70,80],
                      [30,90,40,30]])
multi_arr

#######################################
#Slicing array

#slicing in multi dimentional array
multi_arr[1,2]#70
multi_arr[1,:]#array([40, 50, 70, 90])
multi_arr[:,1]#array([20, 50, 10, 90]) # here it will be consider
#all rows but 1 st column

x=multi_arr[:3,::2]
#rows from 0 to 3 and every alternate column
x
#o/p :-array([[10, 10],
 #            [40, 70],
 #            [60, 70]])

######################################33
#Integer array indexing
arr = np.arange(35).reshape(5,7)
print(arr)

#o/p :- [[ 0  1  2  3  4  5  6]
#        [ 7  8  9 10 11 12 13]
#        [14 15 16 17 18 19 20]
#        [21 22 23 24 25 26 27]
#        [28 29 30 31 32 33 34]]

########################################
#Boolean Array Indexing

#is an array object of Boolean types
#. use this methiod whrn we want to pick elemnts
#from the array which satisify some conditions

arr = np.arange(12).reshape(3,4)
print(arr)
'''o/p: - [[ 0  1  2  3]
           [ 4  5  6  7]
           [ 8  9 10 11]]
    '''
rows = np.array([False,True,True])
#it will not consider oth row as it is false
rows
wanted_rows =arr[rows, :]
print(wanted_rows)

###
rows = np.array([True,False,True])
#it will not consider 1st row as it is false
rows
wanted_rows =arr[rows, :]
print(wanted_rows)

###################################
#Use asarray()

list =[20,40,60,80]
array = np.array(list)
print("Array:",array)
print(type(array))
    
'''o/p:- Array: [20 40 60 80]
<class 'numpy.ndarray'>

'''
#################################33

#Numpy Array Properties

'''
ndarray.shape
ndarray.ndim
ndarray.itemsize
ndarray.size
ndarray.dtype

#Properties dont have open and close parenthesis
'''
#ndarray.shape
#to get the shape of a python Numpy array use numpy
#Shape
array=np.array([[1,2,3],[4,5,6]])
array
print(array.shape)
#o/p :- (2,3)

#Resize the array
array=np.array([[10,20,30],[40,50,60]])
array.shape=(3,2)
print(array)
#o/p :- [[10 20]
#        [30 40]
#        [50 60]]

######################################
#Numpy also provides a numpy.reshape() function to 

#reshape usage
array=np.array([[10,20,30],[40,50,60]])
new_array = array.reshape(3,2)
print(new_array)
'''
o/p:- [[10 20]
      [30 40]
      [50 60]]
'''

#######################################3

#Arithemetic Operations
arr1 = np.arange(16).reshape(4,4)
arr1
arr2 = np.array([1,3,2,4])
arr2

#add()
add_arr = np.add(arr1,arr2)
print(f"Adding two arrays:\n{add_arr}") 

'''o/p:-
Adding two arrays:
[[ 1  4  4  7]
 [ 5  8  8 11]
 [ 9 12 12 15]
 [13 16 16 19]]
'''
#Subtraction()
sub_arr = np.subtract(arr1,arr2)
print(f"Subtracting two arrays:\n{sub_arr}") 
 
'''o/p :-
Subtracting two arrays:
[[-1 -2  0 -1]
 [ 3  2  4  3]
 [ 7  6  8  7]
 [11 10 12 11]]
'''

##Multiplication()
mul_arr = np.multiply(arr1,arr2)
print(f"Multiplying two arrays:\n{mul_arr}") 

'''o/p :-
Multiplying two arrays:
[[ 0  3  4 12]
 [ 4 15 12 28]
 [ 8 27 20 44]
 [12 39 28 60]]
'''

#Division()
div_arr = np.divide(arr1,arr2)
print(f"Dividinging two arrays:\n{div_arr}")

'''o/p :- 
Dividinging two arrays:
[[ 0.          0.33333333  1.          0.75      ]
 [ 4.          1.66666667  3.          1.75      ]
 [ 8.          3.          5.          2.75      ]
 [12.          4.33333333  7.          3.75      ]]
'''

#####################################
#numpy.reciprocal
#This function returns the reciprocal of argumnet
#element wise.Foe element witjh absolute values
#larger than 1,the result is always o

#To perform Reciprococal operation
arr1 = np.array([50,10.3,5,1,200])
rep_arr1=np.reciprocal(arr1)
print(f"After appling reciprocal function to array:\n{rep_arr1}")
'''o/p :- 
After appling reciprocal function to array:
[0.02       0.09708738 0.2        1.         0.005     ]
'''


#numpy.power

#this NumPy power() function treats elements in the first input array
#to perform power operation
arr1=np.array([3,10,5])
pow_arr1=np.power(arr1,3)
print(f"After appling power function to array:\n{pow_arr1}")
'''o/p :-
After appling power function to array:
[  27 1000  125]
'''
arr1=np.array([3,10,5])
arr2=np.array([3,2,1])
print("My second array:\n",arr2)
pow_arr2=np.power(arr1,arr2)
print(f"After appling power function to array:\n{pow_arr2}")

'''o/p :-
After appling power function to array:
[ 27 100   5]
'''

#to perform mod function on NumPy array
import numpy as np
arr1=np.array([7,20,13])
arr2=np.array([3,5,2])
arr1
arr1.dtype
#mod()
mod_arr = np.mod(arr1,arr2)
print(f"After appling mod function to array:\n{mod_arr}")

'''
o/p :-
After appling mod function to array:
[1 0 1]
'''
################################################
#Create an empty array used in image processing
'''error in this code'''
import numpy as np
np.__version__
from numpy import empty
a = empty([3,3])
print(a)

#######################################
#create zero array
from numpy import zeros
a = zeros([3,5])
print(a)
'''o/p :-
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
'''
##############################
#Create one array
from numpy import ones
a = ones([5])
print(a)
'''o/p :-
[1. 1. 1. 1. 1.]
'''

####################################3
#create array with vstack
from numpy import array
from numpy import vstack

#create first array
a1=array([1,2,3])
print(a1)

#create second array
a2=array([4,5,6])
print(a2)

#Vertical Stack
a3=vstack((a1,a2))
print(a3)
print(a3.shape)

#################################### 
#############################
#create array with hstack
from numpy import array
from numpy import hstack

#create first array
a1=array([1,2,3])
print(a1)

#create second array
a2=array([4,5,6])
print(a2)

#Horizontal Stack
a3=hstack((a1,a2))
print(a3)
print(a3.shape)













