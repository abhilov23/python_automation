#working with unicode text file with UTF-8 encoding
file = open('unicode.txt', 'w', encoding="utf-8") #here we usually defines the encoding of the same
file.write('hello, こんにちは') #writing the UTF-8 data into the file
file.close()

#reading a unicode text file from the unicode file
file = open('unicode.txt', 'r', encoding='utf-8') 
data = file.read()
print(data)
