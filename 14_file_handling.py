 #working with the filesystem
 #create a new file
file = open('data.txt', 'w') #opening a file with write permissions
#you can also use other methods like:
# 'w' : write, 'w+' : write and reading
# 'r' : read, 'r+' : read and writing
# 'a' : append, 'a+' : appending and reading
# 'x' : open a file for exclusive creation, if the file already exists, it gives an error

#writing data to the file
file.write('Hello, this is a new text file.\n')
file.write('S   o this is my story and this time i am not going to give up\n')
content = file.read() #reading from the file
print(content) #printing the content of the file
file.close() #to close the file here
