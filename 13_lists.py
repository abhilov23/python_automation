#lists in python
#creating lists
fruits = ['banana', 'apple', 'orange', 'cherry']
number = [1, 2,3,4,5,6,7,8,9,10,11,12]
mixed = ["banana", 45, [54, 5]]

#lets talk about slicing list: [start:end:steps]
print(number[2:6:1]) #3,4,5,6
print(number[:4]) #from starting to 4th position
print(number[4:]) #from 4 to the last elements
print(number[::2])#from the first elements to the last after every two steps


repeated = 2 * fruits 
print(repeated) #it prints the list for two times

#functions in lists
#min() : find the minimum element in the list
#max() : find the maximum element in the list
#sum() : finds the sum of all elements in the list
#sorted() : gives you the shorted list (in alphabetical or numerical order)

