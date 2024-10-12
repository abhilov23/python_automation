#celcius to fahreheit convertor with extra example
#this script convert celcius temp to fahreheit 

celcius_temp = input("enter temprature in celcius:")

celcius_to_fahreheit = 9/5
fahreheit_offset = 32

f =(celcius_to_fahreheit * int(celcius_temp)) + fahreheit_offset

print(f)