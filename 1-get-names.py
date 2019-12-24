
"""
Created on Mon Dec 23 16:28:56 2019

@author: javad
# 
"""

try:
    main_file = open("/home/javad/Documents/codes/blast/398_nt.fasta",'r')
except:
        print('file not found')



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
first_line = main_file.readline()


# get the name of spicies
name = first_line.split("_")[1:3]
name = name[0] + "_" + name[1]

# get the sequence
seq = main_file.readline()

