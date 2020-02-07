
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
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd




try:
    main_file = open("/home/javad/Documents/codes/blast/398_nt.fasta",'r')
except:
        print('file not found')



while True:
    first_line = main_file.readline()
    
    #check for the end of the file
    if ("" == first_line):
        print("file finished")
      #  break #uncomment me
    
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
    try:
        element = WebDriverWait(driver, 20).until(
            EC.visibility_of((By.ID, "searchOptions"))
        )
    finally:
        print("timeout!")
        driver.quit()
        
    #time.sleep(5)
    # it is better to use this type of waits:
    # https://selenium-python.readthedocs.io/waits.html


    # read the table
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find('table' ,attrs={'class':'dscTable ui-ncbigrid'})

    df = pd.read_html(str(table))




    #=========== Do this after deciding how many row need to be selected via bs4 ==========#
    # Deselect_all
    driver.find_element_by_xpath(".//*[contains(text(), 'select all')]").click()

    # tick the checkbox
    i = 1 # select based on the data from the table
    selected_row = driver.find_element_by_id("chk_"+str(i))
    driver.execute_script("arguments[0].click();", selected_row)
    
    
    
    
    # Select the row if e satisfies the condition
    driver.find_element_by_id("deflnDesc_1").click()
    
    # Back to main tab view
    check_list = driver.find_element_by_id("chk_2")
    driver.find_element_by_id("btnDescr").click()

        
    
    

    
