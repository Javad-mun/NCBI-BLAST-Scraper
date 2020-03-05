
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
import os


print("Hi")




column_names = ['Description', 'Max Score', 'Total Score', 'Query Cover', 'E value', 'Per. Ident', 'Accession']
final_df = pd.DataFrame(columns = column_names)


try:
    main_file = open("/home/javad/Documents/codes/blast/398_nt.fasta",'r')
    print("file loaded")
except:
        print('file not found')


ignored_names = list()
no_match_names = list()


first_line = main_file.readline()
current_line = first_line

while ("" != current_line):
    
    # get the name of spicies
    name = current_line.split("_")[1:3]
    name = name[0] + "_" + name[1]
    print("Working on ", name)
    # get the sequence
    seq = main_file.readline()
    
    seq = ">"+ name + "\n" + seq
    
    # read next line for the next loop
    current_line = main_file.readline()

        
    # Create older for the name
    download_dir = "/home/javad/Documents/Ati/ncbi-results/"+name
    try:
        os.mkdir(download_dir)
        calculated_before = False
    except:
        print("folder exists")  
        calculated_before = True
     
    # You might want to use to exclude the species already done
    if os.listdir(download_dir) != []:
        calculated_before = True
    else:
        calculated_before = False
        
            
    try:        
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--private")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("browser.download.folderList",2)
        fp.set_preference("browser.download.dir", download_dir)
        fp.set_preference("browser.download.manager.showWhenStarting", False)
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain")
        
        # Initialize a Firefox webdriver
        driver = webdriver.Firefox(firefox_options=firefox_options, firefox_profile=fp)
        # Grab the web page
        #driver.get("https://blast.ncbi.nlm.nih.gov/Blast.cgi")
        #driver.find_element_by_id("homeBlastn").click()
        driver.get("https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome")
        # https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome 
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
        
    ##    #wait for results for 3 min max
        #time.sleep(30)
        # be careful about the waits. They request and thus refresh the page
    #    try:
    #        element = WebDriverWait(driver, 180).until(
    #            EC.presence_of_element_located((By.ID, "searchOptions"))
    #        )
    #    except:
    #        print(" Cannot get the search results for ", name)
    #        # add name to a list of igonred names
    #        ignored_names.append(name)        
    #    finally:
    #        print("Finished waiting for the results!")
    #        #driver.quit()
    #        
    #   time.sleep(15)
        # it is better to use this type of waits:
        # https://selenium-python.readthedocs.io/waits.html
        # or use implicit waits
        driver.implicitly_wait(180)
        driver.find_element_by_id("searchOptions")
        
    
        # read the table
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = soup.find('table' ,attrs={'class':'dscTable ui-ncbigrid'})
    
        df = pd.read_html(str(table))
        # Now df is a list which has all th table in its 0'th element.
        # convert to df
        df = pd.DataFrame(df[0])
        df.head()
        
        
        
        # decide how many rows we need
        number_of_rows = df.shape[0]
        last_selected_row = 0 # Reset it
        for i in range(number_of_rows):
            query_cov = float(df.iloc[i,4].strip('%'))
            e_value =  df.iloc[i,5]
            query_threshold = 99
            e_threshold =  1e-5
            if (query_cov >= query_threshold and e_value < e_threshold):
                last_selected_row = i
            else:
                break
            
            
        if last_selected_row == 0:
            print(name, " doesn't have any matches")
            no_match_names.append(name)
        else:        
            # Deselect_all
            driver.find_element_by_xpath(".//*[contains(text(), 'select all')]").click()
            time.sleep(3)
        
        
            # tick the checkbox
            # select based on the data from the table
            for i in range(last_selected_row+1):
                selected_row = driver.find_element_by_id("chk_"+str(i+1))
                driver.execute_script("arguments[0].click();", selected_row)
                print(i+1)
                
                
            time.sleep(3)
            # download the text file    
            driver.find_element_by_id("btnDwnld").click()
            time.sleep(5)
            driver.find_element_by_id("dwText").click()
            time.sleep(20) # wait for download
            # Rename the files
            old_file_name = download_dir + "/" +  os.listdir(download_dir)[0]
            os.rename(old_file_name, download_dir + "/" + name + ".txt")
            
            time.sleep(2)
            temp = df.iloc[0:last_selected_row,1:8]
            final_df = pd.concat([final_df, temp])
            try:
                temp.to_csv(download_dir + "/" + name + ".csv")
            except:
                print("file exists")             
            
    except:
        print(" Cannot get the search results for ", name)
        #add name to a list of igonred names
        ignored_names.append(name)  
        
    finally:          
        driver.quit()
        time.sleep(60)
    
    
    
        






# Save final results dataframe and ignored names and names with no match
with open("/home/javad/Documents/Ati/ncbi-results/ignored.txt", 'w') as f:
    for item in ignored_names:
        f.write("%s\n" % item)
        
with open("/home/javad/Documents/Ati/ncbi-results/no-match.txt", 'w') as f:
    for item in no_match_names:
        f.write("%s\n" % item)        

final_df.to_csv("/home/javad/Documents/Ati/ncbi-results/final_results.csv")








 

    
