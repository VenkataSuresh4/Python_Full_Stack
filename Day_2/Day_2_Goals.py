# Print the Header
print("Welcome to the tip calculator.")

# Take the total bill
total_amt = float(input("What was the total bill? $"))

# Input percentage tip
percentage = input("What percentage tip would you like to give? 10, 12, or 15?")

# Number of Persons to split the amt
persons = input("How many people to split the bill?")

percentage_amt = (total_amt * int(percentage)) / 100

individual_amt = round((total_amt + percentage_amt) / int(persons),2)

print(f"Each person should pay {individual_amt}")
