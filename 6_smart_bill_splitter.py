#lets create  a bill spitter script
# total bill:$128
#Number of friends: 5
#goal: Calculate how much each person should pay

#Bonus :
# 1. Include a 15% tip in the total bill before splitting
# 2. Round the individual share to two decimal places (hint: look up to the round() function)

total_bill = 128 
no_of_friends = 5 

#calculate tip
tip = (15 * total_bill) / 100
total_bill = total_bill + tip   #adding the tip in the total bill
per_person = round(total_bill/no_of_friends, 2) #round

print("total bill per person:",per_person )