print("Welcome to the tip calculator.")
bill = float(input("What was the total bill ? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
split = int(input("How many people to split the bill?"))
resault = (bill * (1 + tip / 100)) / split
print(f"Each peroson should pay: ${'{:.2f}'.format(round(resault, 2))}")
