# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 08:37:51 2024

@author: Admin
"""

#Pandas Shuffle DataFrame Rows
'''this process is used in optimization''' 
import pandas as pd
import numpy as np
technologies =({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Hadoop","Spark","Python"],
    'Fees':[20000,25000,26000,22000,np.nan,45000,89000,22000],
    'Duration':['30days','40days','45days','65days','75days','35days','','95days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600],
    })
df=pd.DataFrame(technologies)
print(df)
#Pandas Shuffle DataFrame Rows
#shuffle the DataFrame rows and return all rows
df1 = df.sample(frac =0.5) #shuffle all the rows with 100%
print(df1)

###################################################3
#Create a new Index starting from zero
df1 = df.sample(frac =1).reset_index()
print(df1)

###########################################
#Drop shuffle Index
df1 = df.sample(frac =1).reset_index(drop = True)
#here earlier index will drop it will reinisitate the index
print(df1)

#######################################################
'''SQL'''
import pandas as pd 
technologies = {
    'Courses':["Spark","PySpark","Python","pandas"],
    'Fee':[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days'],
    }
index_labels =['r1','r2','r3','r4']
df1 = pd.DataFrame(technologies,index=index_labels)

technologies2 = {
    'Courses':["Spark","Java","Python","Go"],
    'Discount':[2000,2300,1200,2000]
    }
index_labels2 =['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2,index=index_labels2)

#Pandas Join

'''if we are not mentioning which 
type of join it is by default left join'''

df3= df1.join(df2,lsuffix ="_left",rsuffix="_right")
print(df3)

#o/p:-
'''
Courses_left    Fee Duration Courses_right  Discount
r1        Spark  20000   30days         Spark    2000.0
r2      PySpark  25000   40days           NaN       NaN
r3       Python  22000   35days        Python    1200.0
r4       pandas  30000   50days           NaN       NaN
'''
##########################################
#Pandas Inner Join DataFrame
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='inner')
print(df3)

#o/p :-
'''  Courses_left    Fee Duration Courses_right  Discount
r1        Spark  20000   30days         Spark      2000
r3       Python  22000   35days        Python      1200
'''

##############################################################
#Pandas Left Join DataFrame
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='left')
print(df3)

#o/p:-
'''
Courses_left    Fee Duration Courses_right  Discount
r1        Spark  20000   30days         Spark    2000.0
r2      PySpark  25000   40days           NaN       NaN
r3       Python  22000   35days        Python    1200.0
r4       pandas  30000   50days           NaN       NaN
'''
##############################################################
#Pandas Right Join DataFrame
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='right')
print(df3)

#o/p:-
'''
 Courses_left      Fee Duration Courses_right  Discount
r1        Spark  20000.0   30days         Spark      2000
r6          NaN      NaN      NaN          Java      2300
r3       Python  22000.0   35days        Python      1200
r5          NaN      NaN      NaN            Go      2000
'''
####################################################
#Pandas Merge DataFrames
import pandas as pd 
technologies = {
    'Courses':["Spark","PySpark","Python","pandas"],
    'Fee':[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days'],
    }
index_labels =['r1','r2','r3','r4']
df1 = pd.DataFrame(technologies,index=index_labels)

technologies2 = {
    'Courses':["Spark","Java","Python","Go"],
    'Discount':[2000,2300,1200,2000]
    }
index_labels2 =['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2,index=index_labels2)

#Using pandas.merge()
#it is inner join but it will not reoerte the column 
#courses using merge
df3 = pd.merge(df1,df2)

#Using DataFrame.merge()
df3 = df1.merge(df2)

'''Both give same result'''

##########################################
#Using pandas.concat() to concat two DataFrames
import pandas as pd
df = pd.DataFrame({'Courses':["Spark","PySpark","Python","pandas"],
                   'Fee':[20000,25000,22000,30000]})

df1 = pd.DataFrame({'Courses':["Pandas","Hadoop","Hyperion","Java"],
                   'Fee':[45000,69000,34000,23000]})


#Using pandas.concat() to concat two DataFrames
data = [df,df1]
df2 = pd.concat(data)
df2

#o/p:-
'''
  Courses    Fee
0     Spark  20000
1   PySpark  25000
2    Python  22000
3    pandas  30000
0    Pandas  45000
1    Haddop  69000
2  Hyperion  34000
3      Java  23000
'''

#######################################
#Concatenate multiple DataFrames using pandas.concat()
import pandas as pd
df = pd.DataFrame({'Courses':["Spark","PySpark","Python","pandas"],
                   'Fee':[20000,25000,22000,30000]})

df1 = pd.DataFrame({'Courses':["Unix","Hadoop","Hyperion","Java"],
                   'Fee':[45000,69000,34000,23000]})

df2 = pd.DataFrame({'Duration':['30days','40days','35days','60days','55days'],
                    'Discount':[1000,2300,25000,2000,3000]})

#Apppending multiple DataFrame
df3 = pd.concat([df,df1,df2])
print(df3)

#####################################################################
#Read CSV file into DataFrame

df = pd.read_csv('buzzers.csv')
print(df)

#####################################################3
#Write DataFrame to excel file
df.to_excel('c:/1-python/Bahaman.xlsx')

###########################
#read Excel file
import pandas as pd
df.to_excel('c:/1-python/Bahaman.xlsx')
print(df)

#############################
''''Wrire in notebook'''
#Using Series.values.tolist()
df = pd.DataFrame({'Courses':["Spark","PySpark","Python","pandas"],
                   'Fee':[20000,25000,22000,30000]})
col_list = df.Courses.values #converts data into array form
print(col_list)

col_list = df.Courses.values.tolist()
#converts data into list form
print(col_list)

#####################################3
#Using Series.values.tolist()
col_list = df["Courses"].values.tolist()
print(col_list)

########################
#Using list function
col_list = list(df["Courses"])
print(col_list)

###########################
#Convert to numpy array
import numpy as np
col_list = df["Courses"].to_numpy()
print(col_list)





 





