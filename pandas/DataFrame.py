# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 19:05:16 2022

@author: User
"""

#Importing library
import pandas as pd

#Importing the .txt file
df = pd.read_csv('vaccinations.txt', header = None, skiprows = (1), sep = ',', quotechar = None, quoting = 3)
print(df)

#Getting the 5 first rows of the DataFrame
df.head()
#Getting the 5 last rows of the DataFrame
df.tail()

#Setting a header for the DataFrame
df.columns = ['Country','Country iso code','Date','Total vaccinations',
              'People vaccinated','People fully vaccinated','Total boosters','Daily vaccinations raw',
              'Daily vaccinations','Total vaccinations per hundred','People vaccinated per hundred','People fully vaccinated per hundred',
              'Total boosters per hundred','Daily vaccinations per million','Daily people vaccinated','Daily people vaccinated per hundred']

#Printing the DataFrame
print(df)

#Copying the DataFrame to another DataFrame
df_copy = df.copy()
print(df_copy)

#Deleting one or several columns

#del function for removing one column only
del df_copy['Daily vaccinations']
print(df_copy)

#drop() function for removing one or more columns

#Method 1: Using axis parameter
df_copy_drop1 = df_copy.drop(['Total vaccinations','People vaccinated','Country iso code'], axis=1)
print(df_copy_drop1)

#Method 2: Using columns parameter
df_copy_drop2 = df_copy.drop(columns=['Total vaccinations','People vaccinated','Country iso code'])
print(df_copy_drop2)

#Deleting one or several rows
df_copy_drop = df_copy.drop([100, 525, 9461], axis=0)

#Getting data per country
country = input('Please type your country of interest:')
df_country = df[df['Country'] == country]
print(df_country)

#Exporting DataFrame to Excel
excel_file = df_country.to_excel('Vaccinations by country.xlsx')