# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 20:04:55 2022

@author: User
"""


#Importing library
from urllib import request

#Reading the file from the link
file_url = r'https://github.com/owid/covid-19-data/blob/master/public/data/vaccinations/vaccinations.csv?raw=true'

#Defining a function to download the file
def file_info(url):
    #Opening the url file
    file_open = request.urlopen(url)
    #Reading the file
    file_content = file_open.read()
    #Converting into string
    content = str(file_content)
    #Splitting the lines
    lines = content.split('\\n')
    
    #Saving the data into a text file
    with open('vaccinations.txt', 'w') as output_file:
        for line in lines:
            save_data = output_file.write(line + '\n')
            print(save_data)

#Calling the function
file_info(file_url)