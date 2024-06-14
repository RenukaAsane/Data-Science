# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 08:22:28 2024

@author: Admin
"""
############################################################
#DataFrame
#what is Pandas Dataframe?
#It is  a 2 dimentionsal data structure,
#an imutable,hetrogenous tabular
#data structure with labeled axes rows, and columns
'''install latest version
   >conda install pandas==2.2.1'''
   
   
# to check version
import pandas as pd
pd.__version__

###################################################3
#create using constructor
#create pandas DataFrame from list
import pandas as pd
technologies = [ ["Spark",20000,"30days"],
                ["pandas",20000,"40days"]
                ]
df=pd.DataFrame(technologies)
print(df)

#########################################
#since we have not given labels to column and
#indexes ,Dataframe by default assignms
#incremental sequence number as labels
#to both rows and columns,
#these are called index
#add columns and row labels to the Dataframe
column_names=["Courses","fees","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)
#########################
df.dtypes
#####################################################
#you can also assign custom
#dat types to column
#set custom types to Dataframe
import pandas as pd
technologies ={
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java"],
    'Fees':[20000,25000,26000,22000,24000,45000,89000],
    'Duration':['30days','40days','45days','65days','75days','35days','95days'],
    'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4],
    }
df =pd.DataFrame(technologies)
print(df.dtypes)

#convert all types to best possible types
df2=df.convert_dtypes()#conert obj to string
print(df2.dtypes)

#Change all column to same datatype
df=df.astype(str)#convert str to obj
print(df.dtypes)

#change type for one or multiple columns 
df =df.astype({"Fees": int, "Discount":float})
print(df.dtypes)

########################
#convert data type for all  columns in a list
df = pd.DataFrame(technologies)
df.dtypes
cols = ['Fees','Discount']
df[cols] = df[cols].astype('float')
df.dtypes

##########################3
#ignore errorv
df =df.astype({"Courses": int},errors='ignore')
df.dtypes

#generate error
df =df.astype({"Courses": int},errors='raise')

#covert feed column to numeric type
df = df.astype(str)
print(df.dtypes)
df['Discount'] = pd.to_numeric(df['Discount'])
df.dtypes

###########################################
import pandas as pd
#create DataFrame from dictionary
technologies ={
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java"],
    'Fees':[20000,25000,26000,22000,24000,45000,89000],
    'Duration':['30days','40days','45days','65days','75days','35days','95days'],
    'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4],
    }
df = pd.DataFrame(technologies)
df
###############################
#convert dataframe to csv
df.to_csv('data_file.csv')

##########################
df =pd.read_csv('data_file.csv')

################################
#pandas Dataframe - Basic Operation
#create DataFrame with None/Null to work with example
import pandas as pd
import numpy as np
technologies =({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fees':[20000,25000,26000,22000,np.nan,45000,89000,22000],
    'Duration':['30days','40days','45days','65days','75days','35days','','95days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600],
    })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies, index=row_labels)
print(df)

#################################################
#DataFrame properties
df.shape #imp used in EDA
# (7, 4)
#############################3

df.size
# 28 which is 7x4
#####################
df.columns #imp 
df.columns.values
df.index
df.dtypes #imp
df.info

##############################################################
#Accessing one column content
df['Fees']

####################

#Acessing two column content
df[['Fees','Duration']] 
#or we can write
cols=['Fees','Duration']
df[cols]

####################
#select certain rows to assign it to another dataframe
df2=df[6:]
df2
'''Courses     Fees Duration  Discount
r6   Spark  89000.0               1400
r7  Python  22000.0   95days      1600
'''
df2=df[:6]
df2
df2=df[:7]
df2
# it will print row from 0 to 5

df2=df[:7]
df2


######################################
#accessing certain cell from column "Duration
df['Duration'][3]

#subtracting specific value from a column
df['Fees']=df['Fees']-500
df['Fees']

#################################
#Pandas to manuplate DataFrame 
#Descrine DataaFrame
#Describing DataFrame for all Numeric column
df.describe() #method
#it will show only nueric data from dataframe
#it will show 5 number summery

####################################################
#rename()- Rename DataFrame columns
df = pd.DataFrame(technologies,index=row_labels)

#Acessing new header by setting new column names
df.columns=['A','B','C','D']
df

################################################
#rename column names using rename() method
#whenever u want to make changes to coloumn make axis=1
#for row axis=0
df = pd.DataFrame(technologies,index=row_labels)
df.columns=['A','B','C','D']

#this are three ways to change the columnn name 
df2=df.rename({'A':'c1','B':'c2'},axis=1)
df2
df2=df.rename({'C':'c3','D':'c4'},axis='columns')
df2
df2=df.rename(columns={'A':'c3','B':'c4'})
df2

######################################################
#Drop DataFrame rows and columns
df = pd.DataFrame(technologies,index=row_labels)

#drop rows by lables
df1 = df.drop(['r1','r2'])
df1

#Deletings rows by posinon or index
df1=df.drop(df.index[1])
df1

df1=df.drop(df.index[[1,3]])
df1

#deleting rows by index
df1=df.drop(df.index[2:]) #it will drop from 2 index
df1

#when u have defult indexes for rows
df = pd.DataFrame(technologies)
df1= df.drop(0)
df1 

df = pd.DataFrame(technologies)
df1=df.drop([0,3],axis=0)
#it will delet row0 n row3
df1

df1=df.drop(range(0,3))
#it will delet 0 and 2
df1

##############################################
#Dropping of columns

import pandas as pd
import numpy as np
technologies =({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fees':[20000,25000,26000,22000,np.nan,45000,89000,22000],
    'Duration':['30days','40days','45days','65days','75days','35days','','95days'],
    })
df=pd.DataFrame(technologies)
print(df)
#Drop column by name
#Drop 'Fees' column
df2=df.drop(["Fees"],axis=1)
print(df2)


#Explicitely using parameter name 'label'
df2=df.drop(labels=["Fees"],axis=1)

#3Alternatively u can also use colmns instead of label
df2=df.drop(columns=["Fees"],axis=1)

##########################################
#Drop column by index
print(df.drop(df.columns[1],axis=1))

df=pd.DataFrame(technologies)

#using inplace=True
df.drop(df.columns[2],axis=1,inplace=True)
#inplace = True will make change to original copy 
#it will not change its duplicate copy but original
#copy
print(df)

###########################################
df=pd.DataFrame(technologies)
#Drop 2 or more columns by label name
df2=df.drop(["Courses","Fees"],axis = 1)
print(df2)

##############################################
#Drop 2 or more columns by Index
#whenever we are droping more than 1 columns we 
#need to write list inside list
df=pd.DataFrame(technologies)
#DataFrame will be in original state

df2=df.drop(df.columns[[0,1]],axis=1)
print(df2) #it will drop fees and coures column

#############################################
'''Wite it in ready reference part of notebook'''
#Drop column from list of Columns
df = pd.DataFrame(technologies)
df.columns
lisCol =["Courses","Fees"]
df2=df.drop(lisCol, axis =1)
print(df2) 

################################################3
#Remove columns from DataFrame inplace
df=pd.DataFrame(technologies)
df.drop(df.columns[1],axis=1,inplace=True)
#it will remove 0 and 2 index columns
df

#using inplace=True
'''write in interview que
whenever u want to acces column using index use
iloc and if by name use loc 
in sliceing we no need to give coma but in iloc we need to give coma'''
################################################
################################################
#Pandas select rows by index (Position/Label)
#use of index
import pandas as pd
import numpy as np
technologies =({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fees':[20000,25000,26000,22000,np.nan,45000,89000,22000],
    'Duration':['30days','40days','45days','65days','75days','35days','','95days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600],
    })

row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies , index=row_labels)
print(df)

#df.iloc[startrow:endrow,startcolumn:endcolumn]

df=pd.DataFrame(technologies,index=row_labels)
#Below are quick example 
df2=df.iloc[:,0:2]
df2

#This line use the slicing operation to et DataFrame
#item by index
#The first slice [:] indicates to returm 1of DataFrame
#the second slice specifies that only columns
#between 0 and 2 (excluding 2) should be returned

##########################################3

df2=df.iloc[0:2,:]
df2

#in this case the first slice [0:2] is
#requesting onlu 0 through 1of the DataFrame
#The seconf slice [:] indicates that all columns are required

#slicing specifies Rows and Columns using iloc attribute
df3=df.iloc[1:2,1:3]
df3

#Another example
df3=df.iloc[:,1:3]
df3

#The 2 nd operator [1:3] yields columns 1 and 3 only
#Select Rows by Integer Index
df2=df.iloc[2]  #select row by index
df2

#to access 3 or more rows from lisrt inside list

df2=df.iloc[[2,3,6]] #select row by index list
df2=df.iloc[1:5]#select row by integer index range
df2=df.iloc[:1] #select first row
df2=df.iloc[:3] #select first 3 rows
df2=df.iloc[-1:] #select last row
df2=df.iloc[-3:] #select last 3 rows
df2 = df.iloc[::2] #select alternate rows

#select rows by Index Labels
df2=df.loc[['r2']]  #select row by label
df2
df2 = df.loc[['r2','r3','r6']]#select rows by index label
df2 = df.loc['r1':'r5']#select  rows by label index
df2 = df.loc['r1':'r5':2]#select alternate rows with index
#2 is for selec tion of every alternate columns
###############################################
#Pandas Select columns by Name or Index
#By using df[] Notations
df2=df['Courses']

##select multiple columns
df2=df[['Courses','Fees','Duration']]

#Using loc[] to take column slice
#loc[] syntax to slice columns
#df.loc[:,start:stop:step]
##Select multipe columns
df2 = df.loc[:,['Courses','Fees','Duration']]
#select Random columns
df2 = df.loc[:,['Courses','Fees','Duration']]
#Selct columns between 2 columns
df2 = df.loc[:,'Fees':'Discount']
##Select columns by range
df2 = df.loc[:,'Duration':]

#select column by range
#All columns upto 'Duration column
df2 = df.loc[:,:'Duration']

#select every alternate columns
df2 = df.loc[:,::2]

####################################################3
#Pandas .DataFrame.query() by examples
#Query all rows with Courses equals 'Spark'
#hwere spark should be in single quotes if 
#you are usiong double quotes there will be error
df2=df.query("Courses == 'Spark'")
print(df2)

#not equals condition
#it will give all row without spark
df2 = df.query("Courses != 'Spark'")
df2

##########################################33
import pandas as pd
import numpy as np
technologies =({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas"],
    'Fees':[20000,25000,26000,89000,22000],
    'Discount':[0.1,0.2,0,0.5,0.1]
    })

df=pd.DataFrame(technologies)
print(df)
###################################################3
#Pandas adding column  to DataFrame
#Add new column to the DataFrame
tutors =['Ram','sham','Ghansham','Ganesh','Ramesh']
df2 = df.assign(TutorsAssigned=tutors)
print(df2)

##########################################################
#Adding multiple columns to DataFrame
MNCCompanies = ['TATA','HCL','Infosys','Google','Amazon']
df2 = df.assign(MNC=MNCCompanies,tutors=tutors)
df2

#######################################################3
#Derive New Column from Existing Column
df = pd.DataFrame(technologies)
df2=df.assign(Discount_Percent=lambda x: x.Fees * x.Discount /100)
print(df2)

#########################################################
#Appemnd Columns to Existing Pandas DataFrame
#Add New column to the existing DataFrame
df = pd.DataFrame(technologies)
df['MNCCompanies'] = MNCCompanies
print(df)

######################################################33
#Add new column to the specific position
df = pd.DataFrame(technologies)
df.insert(0,'Tutors',tutors)
print(df)

########################################
########################################
#Pandas Rename column with example
import pandas as pd
import numpy as np
technologies =({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java"],
    'Fees':[20000,25000,26000,89000,22000,35000,45000],
    'Duration':['30days','40days','45days','65days','75days','35days','95days']
    })

df=pd.DataFrame(technologies)
print(df)
print(df.columns)

#Pandas Rename column name
#Rename Multiple columns
df2=df.rename( 'Courses':'Courses_List' ,axis =1)
df2=df.rename('Courses':'Courses_List' ,axis ='columns')

#######################################################
'''in order to change columns of existing DataFrame
without coping to the new DataFrame,
you have to use inplace=true
replace existing DataFrame (inplace).This returns None
'''
df.rename( column={'Courses':'Courses_List' ,'columns',inplace =True})
print(df.columns)

###############################################################

#Quick examples of get the number of Rows in DataFrame
rows_count = len(df.index)
rows_count
rows_count = len(df.axes[0])
rows_count
column_count = len(df.axes[1])
column_count

##########################################################
df=pd.DataFrame(technologies)
row_count = df.shape[0] #Returns number of rows
row_count
col_count = df.shape[1] #Return number of columns
print(row_count)
print(col_count)
#o/p :- 7
#       3

#########################################################
#Pandas Apply Function to a column
#Below are quick examples
#using DataFrame.apply() to apply function add column

import pandas as pd
import numpy as np

data={"A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]
      }

df=pd.DataFrame(data)
print(df)

def add_3(x):
    return x+3
df2=df.apply(add_3)
df2
df2=((df.A).apply(add_3))

#############################################3
#Using apply function single column
def add_4(x):
    return x+4
df["B"] = df["B"].apply(add_4)
df["B"]

#Apply to multiple columns
df[['A','B']]= df[['A','B']].apply(add_4)
df

#Apply a lambda function to each column
df2=df.apply(lambda x : x+10)
df2

################################################

#Apply lambda fun to a single column
#using dataframe.apply() and lambda function
df["A"]=df["A"].apply(lambda x: x-2)
df

####################################################
#Using pandas.DataFrame.transform() to apply function column
#usinf dataFrame.transform()
def add_2(x):
    return x+2
df = df.transform(add_2)
print(df)

###########################################333
#Using pandas .DataFrame.map() to single column

df['A'] = df['A'].map(lambda A: A/2.)
print(df)

#####################################3
#Using Numpy function on single column
#usinf DataFrame.apply()  & [] operator

df=pd.DataFrame(data)
import numpy as np
df['B'] = df['B'].apply(np.square) #on column B
print(df)

########################################
#secod method to apply square method on column
#Using NumPy.square() Method
#Using numpy.square()adnd [] operato
df=pd.DataFrame(data)
df['A'] = np.square(df['A']) #on column A
print(df)

##########################################
#Pandas groupby() with Examples
import pandas as pd
technologies =({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Hadoop","Spark","Python"],
    'Fees':[20000,25000,26000,22000,np.nan,45000,89000,22000],
    'Duration':['30days','40days','45days','65days','75days','35days','','95days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600],
    })
df=pd.DataFrame(technologies)
print(df)

#Using groupby() to compute the sum
df2 = df.groupby(['Courses']).sum()
print(df2)

###################################################
#Group by multiple columns
df2= df.groupby(['Courses','Duration']).sum()
print(df2)

###################################################
#Add index to the grouped data
#Add Row Indexto the group by result
df2 = df.groupby(['Courses','Duration']).sum().reset_index()
print(df2)

####################################################
#Get the listof all column names from header
'''Here something is remaining do check'''

column_headers = list(df.columns.values)
print("The column header:",column_headers)

#Using list(df) to get column headers as a list 
column_headers = list(df.columns)
column_headers

#Using list(df) to get the list of all column names
column_headers = list(df)
column_headers

###################################################
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
df1 = df.sample(frac =1)
print(df1)

##############################################

