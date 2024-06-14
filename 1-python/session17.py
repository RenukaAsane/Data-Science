# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 08:23:54 2024

@author: Admin
"""
#########################################
#index array out of bounds
from numpy import array
#define array
data=array([11,22,33,44,55])
#index data
print(data[5])
#o/p :- index 5 is out of bound for axis 0 with size 5 

###########################################33
#index row of two-dimentonal array
from numpy import array
#define array
data = array([
    [11,22],
    [33,44],
    [55,66]])
#index data
print(data[0,])#0th row and all column

#o/p :- [11,22]

#####################################3
#slice a one dimentional array
from numpy import array
#define array
data = array([11,22,33,44,55])
print(data[1:4])
#o/p := [22,33,44]

##############################3
#negative slicing fo a 1-d array
from numpy import array
#define array
data =array([11,22,33,44,55])
print(data[-2:])
#o/p :- [44 55]

#########################
#split input and output data
'''write in prepartion'''
from numpy import array
#define array
data = array([
    [11,22,33],
    [44,55,66],
    [77,88,99]])
#seperate data
x,y = data[:,:-1], data[:,-1]
x
y
#data[:, :-1] - all rows and columns 0 and 1
#all rows and last column

#################################################3
#broadcast scalar to 1-d array
#when there is only number i.e 2 it is scalar
#if it is [1,2,3] it is vector
from numpy import array
#define array
a =array([1,2,3])
print(a)
#define  scalar
b=2
print(b)
#broadcast
c = a + b
print(c)

############################################3
'''
Vector L1 Norm
The L1 norm is calculated as the sum of the absolute 
vector values,where the absolute value a scalar
uses the notation |a1|. 
In effect, the norm is a calculation of the 
Manhattan distance from the original of the vector space
||v||1 = |a1| + |a2| + |a3
'''
from numpy import array
from numpy.linalg import norm
#define vector
a = array([1,2,3])
print(a)
#calculate norm
l1 = norm(a,1)
print(l1)

#######################################################

#Vector L2 norm

'''
The notation for the L2 norm of a vector x is
||x||power of 2.
Another name for L2 norm of a vector
is Euclidean distance.
This is often used for calculating
the error in machine learning models
'''
from numpy import array
from numpy.linalg import norm
#define vector
a = array([1,2,3])
print(a)
#calculate norm
l2 = norm(a)#root of 1,2,3 square i.e 1,4,9=14 under root of 14 is 3.74
print(l2)

#################################################
#Properties of Matrices
#Trangular matrices
from numpy import array
from numpy import tril
from numpy import triu
#define square matrix
M = array([
    [1,2,3],
    [1,2,3],
    [1,2,3]])
print(M)

#lower trangular matrix
lower = tril(M)
print(lower)
#upper trangular matrix
upper = triu(M)
print(upper)

##############################################
#diagonal matrix
from numpy import array
from numpy import diag
#define square matrix
M = array([
    [1,2,3],
    [1,2,3],
    [1,2,3]])
print(M)
#extract diagonal vector
d = diag(M)
print(d)
'''o/p:-[1 2 3]'''
#create diagonal matrix from vector
D = diag(d)
print(D)
'''o/p :- [[1 0 0]
           [0 2 0]
           [0 0 3]]
'''

####################################
#identity matrix
from numpy import identity
I = identity(3)
print(I)

###########################################
#orthogonal matrix
'''
The matrix is said to be an orthogonal matrix
if the product of a matrix and its transposr 
gives an identity value
'''

from numpy import array
from numpy.linalg import inv
#define othogonal matrix
Q = array([
    [1,0],
    [0,-1]])
print(Q)
#inverse equivalence
V = inv(Q)
print(Q.T)
print(V)
#identity equivalance
I = Q.dot(Q.T)
print(I)

#####################################################
from numpy import array
#define matrix
A = array([
    [1,2],
    [3,4],
    [5,6]])
print(A)
#calculate transopse
C=A.T
print(C)
'''o/p:- [[1 3 5]
          [2 4 6]]'''

#############################
#inverse matrix
from numpy import array
from numpy.linalg import inv
#define matrix
A=array([
    [1.0,2.0],
    [3.0,4.0],
    ])
print(A)
#o/p :- [[1. 2.]
#       [3. 4.]]
#inverse matrix
B = inv(A)
print(B)
#o/p :-[[-2.   1. ]
#       [ 1.5 -0.5]]

#multiply A and B
I =A.dot(B)
print(I)

'''o/p :-[[1.00000000e+00 1.11022302e-16]
         [0.00000000e+00 1.00000000e+00]] '''

########################################
#sparse matrix- the matrix which has number of zero's
from numpy import array
from scipy.sparse import csr_matrix
#create dense matrix
A = array([
    [1,0,0,1,0,0],
    [0,0,2,0,0,1],
    [0,0,0,2,0,0]])
print(A)
#convert to sparse matrix (CSR method)
S = csr_matrix(A)
print(S)
#o/p :- (0, 0)	1
#       (0, 3)	1
#       (1, 2)	2
#       (1, 5)	1
#       (2, 3)	2

#reconstruct dense matrix
B = S.todense()
print(B)

#########################################















