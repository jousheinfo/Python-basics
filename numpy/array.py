# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 21:24:10 2022

@author: User
"""

#Importing libraries
import numpy as np
import pandas as pd

#Importing the .txt file
df = pd.read_csv('vaccinations.txt', header = None, skiprows = (1), sep = ',', quotechar = None, quoting = 3)
print(df)

#Converting the DataFrame into array
array_data = np.array(df)
print(array_data)                 

#Selecting the first 5 rows (from 0 to 4)
first_rows = array_data[:5,:]
print(first_rows)

#Selecting the first 4 columns (from 0 to 3)
first_columns = array_data[:,:4]
print(first_columns)

#Copying the array to another array
array_copy = array_data.copy()
print(array_copy)

#Removing one or multiple columns
delete_columns = np.delete(array_data, [2,7,11], axis=1)
print(delete_columns)

#Removing one or multiple rows
delete_rows = np.delete(array_data, [100, 525, 9461], axis=0)
print(delete_rows)

#Comparing arrays

#Getting the number of columns
rows1 = np. size(array_data, 1)
print(rows1)
rows2 = np. size(delete_columns, 1)
print(rows2)

#Getting the number of rows
columns1 = np. size(array_data, 0)
print(columns1)
columns2 = np. size(delete_rows, 0)
print(columns2)

#Getting data per country (Selecting all rows where the first column is equal to 'country')
country = input('Please type your country of interest:')
array_data_country = array_data[array_data[:,0] == country]
print(array_data_country)

#Exporting array to Excel

import xlsxwriter

#Creating the Excel file

#Creating the workbook
workbook = xlsxwriter.Workbook('Vaccinations by country.xlsx')
#Creating the worksheet
worksheet = workbook.add_worksheet()

#Creating a list for the header in Excel
header = ['Country','Country iso code','Date','Total vaccinations','People vaccinated','People fully vaccinated','Total boosters','Daily vaccinations raw','Daily vaccinations','Total vaccinations per hundred','People vaccinated per hundred','People fully vaccinated per hundred','Total boosters per hundred','Daily vaccinations per million','Daily people vaccinated','Daily people vaccinated per hundred']

#Iterating over the header to create the first row in Excel
row_header = 0
for column_header, data_header in enumerate(header):
    worksheet.write(row_header, column_header, data_header)
    
#Iterating over the array data to export to Excel
column = 0

for row, data in enumerate(array_data_country):
    try:
        worksheet.write_row(row+1, column, data)
    except:
        pass
    
workbook.close()