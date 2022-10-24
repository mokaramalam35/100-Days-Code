print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
total_people = int(input("How man people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

tip_amount = float((bill * tip)/100)
split_bill = "{:.2f}".format((bill + tip_amount)/total_people)
print(f"Each person should pay: ${split_bill}")