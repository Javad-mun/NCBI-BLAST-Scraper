#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 17:50:10 2019

@author: javad
"""
import pandas as pd
import os
os.getcwd()


# convert the object from selenium to a soup object instead of reading from the disk
from bs4 import BeautifulSoup

with open("output1.html", "r") as fp:
    soup = BeautifulSoup(fp)

# find the table 
table = soup.find('table' ,attrs={'class':'dscTable ui-ncbigrid'})

df = pd.read_html(str(table))

e_list = table.find_all('td',attrs={'class':'c6'})



# Deselect_all
driver.find_element_by_xpath(".//*[contains(text(), 'select all')]").click()

# Use this to conver to pandas
# Read the table to pd data frame and select the first row and check if it matches the query
https://stackoverflow.com/questions/50633050/scrape-tables-into-dataframe-with-beautifulsoup/50633450
    

# selecting top five and e values less than threshold
for i in range(0,5):
    try:
        print(float(e_list[i].renderContents())) # comment me
        
        e_value = float(e_list[i].renderContents())
        
        e_threshold = 0.001
        if e_value < e_threshold:
            # go back to selenium driver and
            # select the row    
            print("selected")
            # tick the checkbox
            selected_row = driver.find_element_by_id("chk_"+str(i))
            driver.execute_script("arguments[0].click();", selected_row)
    
            
            
            
            
    except:
        print("something is wrong but don't worry, we will continue")
        
        
    
    
    # Go to selenium driver and click on text
    # Also on FASTA
    # Also save the drive
        
        
        
        
""" 
for downloading files:
    29

Here's a solution. Set Firefox's preferences to save automatically, and not have the downloads window popup. Then you just grab the file, and it'll download.

So, something like this:

FirefoxProfile fxProfile = new FirefoxProfile();

fxProfile.setPreference("browser.download.folderList",2);
fxProfile.setPreference("browser.download.manager.showWhenStarting",false);
######## change this ########## created different folders and download in each folder
fxProfile.setPreference("browser.download.dir","c:\\mydownloads");
fxProfile.setPreference("browser.helperApps.neverAsk.saveToDisk","text/csv");

"""
        
        
        
    
    
