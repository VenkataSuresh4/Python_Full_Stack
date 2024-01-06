# Roller Coaster
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
total_bill = 0
if height >= 120:
    print("You can ride the Roller Coaster")
    age = int(input("What is your age?\n"))
    if age < 12:
        total_bill += 5
        print(f"Child tickets are $5")
    elif age <= 18:
        total_bill += 12
        print(f"Youth tickets are $12")
    elif age >= 45 and age < 55:
        print("Everything is going to be Ok. Have a free ride on us!")
    else:
        print(f"Adult tickets are $7")
        total_bill += 7

    want_photos = input("Do you want photos? Yes or No \n")

    if want_photos == "Yes":
        total_bill += 3

    print(f"The total bill is ${total_bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Even or Odd Number
number = int(input())

if number % 2 == 0:
    print(f"{number} is an Even Number")
else:
    print(f"{number} is a Odd Number")

# BMI Calculator
bmi_height = float(input("Height(m) : "))
bmi_weight = int(input("Weight(kg) : "))

bmi = float(int(bmi_weight) / (float(bmi_height) ** 2))

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")

# Leap Year
year = int(input("Provide the Year: \n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a Leap Year")
        else:
            print(f"{year} is not a Leap Year")
    else:
        print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")

# Pizza Delivery Process
print("Thank you for choosing Python Pizza Delivers!")
size = input("What size pizza do you want? S, M, or L")
add_pepperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra chesse? Y or N")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${total_bill}")


# Love Calculator
print("The Love Calculator is calculating your score....")
name1 = input().lower()
name2 = input().lower()

total_name = name1 + name2

T = total_name.count("t")
R = total_name.count("r")
U = total_name.count("u")
E = total_name.count("e")

L = total_name.count("l")
O = total_name.count("o")
V = total_name.count("v")
E = total_name.count("e")

percentage = int(str(T + R + U + E) + str(L + O + V + E))

if percentage < 10 or percentage > 90:
    print(f"Your score is {percentage}, you got together like coke and mentos.")
elif percentage > 40 and percentage < 50:
    print(f"Your score is {percentage}, you are alright together.")
else:
    print(f"Your score is {percentage}.")

