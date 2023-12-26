# Data Types

# String - SubScripting

print("Hello")
print("Subscript : " + "Hello"[0])

# Integer

print(3)
print(type(3))

# Float

print(3.12)
print(type(3.12))

# Boolean

print(True)
print(False)

name_length = len(input("What is your name?\n"))
print(str(name_length) + " Characters")

print(float(100))
print(int(100.23))
print(str(200) + " Chocolates")

# Interactive Exercise
two_digit_number = input()
total = int(two_digit_number[0]) + int(two_digit_number[1])
print(total)

# Mathematical Operators
3 + 1  # Addition
4 - 1  # Subtraction
5 * 2  # Multiplication
6 / 3  # Division
7 ** 2  # Power

# PEMDAS
# Paranthesis - ()
# Exponential - **
# Multiplication - *
# Division - /
# Addition - +
# Subtraction - -

print((2 * 3) ** 2 * 2 / 2 + 10 - 12)

# Interactive Exercise - BMI Calculator bmi = weight / height ^2

height = input()
weight = input()

bmi = int(int(weight) / (float(height) ** 2))

print(bmi)

# Interactive Exercise - F String - Left Weeks

age = input()
pending_age = 90 - int(age)
pending_weeks = pending_age * 52
print(f"You have {pending_weeks} weeks left.")