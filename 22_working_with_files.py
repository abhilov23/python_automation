#steps to work wwith the files
#1. open the file using open() method
#2. perform the task 
#3. clos the file using close() method

file = open('sample.txt', 'r') #opening the file in read mode
filecontent = file.read() #to read that specific file
print(filecontent)
file.close()

readlines() #for reading multiple lines means complete file
readline()#for reading 1 line
file.close() 

#lets talk about write mode
file = open('sample.txt', 'w') #w defines the write mode
#write mode opens the file and write it from the scratch

file.write('Hello, this is a new text file.\n')
file.write('This is my second line.\n')
file.close()

#append mode : starts write the file in the existing content of the file.
#and do not erases the other content of the same.

file = open('sample.txt', 'a')
file.write('This is the third line.\n')
file.close()

#in the above example, we have opened the file in 'write' and 'append' mode,
os.remove(filepath) #to remove this file, but it can remove anything so 
# we can use other method like
os.remove.isfile(filepath)