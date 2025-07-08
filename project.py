# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 08:13:14 2025

@author: user
"""

import  pandas as  pd 
import  numpy  as  np
import matplotlib.pyplot as plt

df=pd.read_csv(r'C:\Users\user\Downloads\archive (7)\marksheet.csv')##  load the  file
print(df.head())##  first five elements
print(df.info())#to  check is  there any  null  characters

## have  to  find  the  total. so create a  new  column
df['total']=df['Science']+df['English']+df['History']+df['Maths']
print(df)

## finding  the  average marks  to  calculate  the students  overall  performance
df['Average']=round(df['total']/4)
print(df)

##check  how  many students  are  above 80% or  A++  students 
count = (df['Average'] > 80).sum()
print("number  of  students  with  above  average 80 %:", count)
##chek  how many students  are  below  40% or W students
coun = (df['Average'] <40).sum()
print("number of  students with below  average 40 %:",coun)

## divide  genders
cf=df['Gender'].value_counts()
print(cf)

##check which  age  group  performed well
gender_perf = df.groupby('Gender')['total'].mean()
print("Average total marks by gender:\n", gender_perf)

##check  which age  group performed  well
age_perf=df.groupby("Age")['total'].mean()
print("Average total marks by age",age_perf)

##check  which  subject  performed  well
sub1=df['History'].mean()
print("Average  performance by History",sub1)
sub2=df['Maths'].mean()
print("Average  performance by Maths",sub2)
sub3=df['Science'].mean()
print("Average  performance by Science",sub3)
sub4=df['English'].mean()
print("Average  performance by English",sub4)

##visuvalisation findings

gender_perf.plot(kind='bar', color='red')
plt.title('Average Total Marks by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Marks')
##plt.grid(True, axis='y', alpha=0.7)
##plt.tight_layout()
plt.show()

age_perf.plot(kind='bar', color='lightgreen')
plt.title('Average Total Marks by Age Group')
plt.xlabel('Age')
plt.ylabel('Average Marks')
##plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

cf.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightskyblue'])
plt.title('Gender Distribution')
plt.ylabel('')  # Hide y-label
plt.tight_layout()
plt.show()











