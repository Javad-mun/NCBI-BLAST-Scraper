#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 17:50:10 2019

@author: javad
"""

import os
os.getcwd()


# convert the object from selenium to a soup object instead of reading from the disk
from bs4 import BeautifulSoup

with open("output1.html") as fp:
    soup = BeautifulSoup(fp)

# find the table 
table = soup.find('table' ,attrs={'class':'dscTable ui-ncbigrid'})


e_list = table.find_all('td',attrs={'class':'c6'})


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
        
        
        
    
    
