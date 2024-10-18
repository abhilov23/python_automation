#In this section, we are going to work on the binary part of the files.

binary_file = open('data.bin', 'wb')#reading a binary data
# 'wb' is for binary data
binary_data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08' #here is the binary data
binary_file.write(binary_data) #writing the binary data into the things
binary_file.close() #closing the function

binary_data = open('data.bin', 'rb') #'rb' is for read binary
data = binary_data.read() #reading the binary data using read methods
print(data) #writing the binary data
binary_file.close() #closing the binary file