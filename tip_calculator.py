#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = input("What was the the bill? $  ")
num_people = input("How many people were in the party?  ")
tip = input("How much would you like to tip? (number percentage)  ")

tip_calc = 1 + .01 * float(tip) 
bill_per_person = (float(bill) /int(num_people))

owed_amount = round(bill_per_person * tip_calc, 2)

print(f"Each person should pay: ${owed_amount}")
