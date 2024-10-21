#shutil module offers other functionality for the file manipulation in
#python

#check the hand written notes for more
import os 


import shutil 

# path 
path = 'C:/Users/ksaty/csv/gfg'

print("Before copying file:") 
print(os.listdir(path)) 

# Source path 
src = 'C:/Users/ksaty/csv/gfg'

# Destination path 
dest = 'C:/Users/ksaty/csv/gfg/dest'

# Copy the content of 
# source to destination 
destination = shutil.copytree(src, dest) 

print("After copying file:") 
print(os.listdir(path)) 

# Print path of newly 
# created file 
print("Destination path:", destination) 
 