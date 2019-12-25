
"""
Created on Mon Dec 23 16:28:56 2019

@author: javad
# 
"""



# repeat these till file has lines
        
        
"""
Created on Mon Dec 23 16:28:56 2019

@author: javad
# 




while True:
    line = f1.readline()
    print line
    if ("" == line):
        print "file finished"
        break;
"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup




try:
    main_file = open("/home/javad/Documents/codes/blast/398_nt.fasta",'r')
except:
        print('file not found')



while True:
    first_line = main_file.readline()
    
    #check for the end of the file
    if ("" == first_line):
        print("file finished")
        break
    
    # get the name of spicies
    name = first_line.split("_")[1:3]
    name = name[0] + "_" + name[1]
    
    # get the sequence
    seq = main_file.readline()
    
    seq = ">"+ name + "\n" + seq
    
    # name and seq are ready
    
    # Initialize a Firefox webdriver
    driver = webdriver.Firefox()
    # Grab the web page
    driver.get("https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome")
        
    # fill the seq section named as QUERY
    seq_box = driver.find_element_by_name("QUERY")
    seq_box.send_keys(seq)   
    
    name_box = driver.find_element_by_name("JOB_TITLE")
    name_box.click()
    
    # Access advance setting
    adv_setting = driver.find_element_by_id("algPar")
    adv_setting.click()
    
    word_size = Select(driver.find_element_by_name("WORD_SIZE"))
    word_size.select_by_visible_text("16")
    
    #submit key
    blast_key = driver.find_element_by_id("b2")
    blast_key.click()
    
    #wait for results
    time.sleep(5)
    # it is better to use this type of waits:
    https://selenium-python.readthedocs.io/waits.html
    
    
    doc = BeautifulSoup(driver.page_source, 'html.parser')

    with open("output1.html", "w") as file:
        file.write(str(doc))
        
        
        
        
    
    

    
