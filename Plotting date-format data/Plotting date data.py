# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 19:26:42 2022

@author: User
"""


#Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates

#Reading the text file
df = pd.read_csv('vaccinations.txt', header = None, skiprows = (1), sep = ',', quotechar = None, quoting = 3)
print(df)

#Setting a header for the DataFrame
df.columns = ['Country','Country iso code','Date','Total vaccinations',
              'People vaccinated','People fully vaccinated','Total boosters','Daily vaccinations raw',
              'Daily vaccinations','Total vaccinations per hundred','People vaccinated per hundred','People fully vaccinated per hundred',
              'Total boosters per hundred','Daily vaccinations per million','Daily people vaccinated','Daily people vaccinated per hundred']

#Printing the DataFrame
print(df)

#Getting data per country
country = input('Please type your country of interest:')
df_country = df[df['Country'] == country]
print(df_country)

#Plotting

#Converting date to datetime format
df_country['Date'] = pd.to_datetime(df_country['Date'])
df_country.sort_values('Date', inplace=True)

#Choosing the plot style
plt.style.use('seaborn')

#Setting the axis values
x = df_country['Date']
y = df_country['People fully vaccinated']

#Making the graph
plt.plot_date(x,y)

#Giving date format to the x-axis
plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter('%d-%m-%Y')
plt.gca().xaxis.set_major_formatter(date_format)
plt.tight_layout()
plt.xlabel('Date')
plt.ylabel('People fully vaccinated')
plt.title('Vaccinations')
plt.show()