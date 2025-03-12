print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
compute_tip = float((bill / people) * (float(tip / 100 + 1)))

total_tip = round(compute_tip,2)
print(f" Each person should pay: ${total_tip}")
