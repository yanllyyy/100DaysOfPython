print("Welcome to the tip calculator!")
amount = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
person = int(input("How many people to split the bill? "))
total_amount = (amount+(tip*amount*0.01))/person
print("Each person should pay: $"+ str(total_amount))