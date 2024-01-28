# Create a function for Greet

def greet():
    print("Good Morning")
    print("How are you doing")
    print("I am doing great")


greet()


# Function with Input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you doing {name}?")


greet_with_name("Suresh")


# Function with multiple input
def greet_from_location(name, location):
    print(f"Hi {name}")
    print(f"When did you return from {location}")


greet_from_location("Suresh", "America")

greet_from_location(location="Russia", name="Alekhya")

import math


def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    print(f"You'll need a {math.ceil(number_of_cans)} cans of paint.")


# Dont change the code below
test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


def prime_check(number):
    count = 0
    for value in range(2, number):
        if number % value == 0:
            count += 1
            print(f"{number} is divisible by {value}")

    if count > 1:
        print(f"{number} is not a prime number")
    else:
        print(f"{number} is a prime number")


n = int(input())
prime_check(number=n)