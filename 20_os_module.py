#handling the OS module

import os 
c = os.path.join('usr', 'bin','home') #this method will join all the files to each other
print(c) #like this /usr/bin/home

print(os.getcwd()) #shows the current workking directory
os.chdir('D:/Programs') #this can change the current working directory
print(os.getcwd()) 