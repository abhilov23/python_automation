import os
#makedirs will create a folder in the specific directory

os.makedirs('D://Programs//testing')
#so basically we creatinng a testing directory, you can also creating directory
#and sub-directory inside that using this command 
print(os.path.abspath('./18_loops.py')) #RETURNS The absolute path of relative file
print(os.path.relpath('d://program')) #Returns the relative path of absolute file

os.path.isabs() #to check if the path is absolute or not

os.path.basename(path) #to check the base-file-name of the path 
#for ex: C:abc/xyz.txt  => xyz.txt

os.path.split(xyz) #splits the filepath into chunks

os.path.getsize(path) #gets the size of the specific file

x = os.listdir(path) #to get the list of files in that specific directory
print(x)

os.path.exists(path) #to check if the path exists or not
#this function returns true if it exists and false if it is not 
#but the thingis  that it will help you to check for the things so that
#your program will not crash like others

os.path.isdir(path) #to check if the path is directory or not
os.path.isfile(path) #to check if it is a file or not
