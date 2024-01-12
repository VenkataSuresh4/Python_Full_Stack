# # For Loop Training
#
# fruits = ["Apple", "Pears", "Oranges"]
#
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")

# # Students average height
# student_heights = input().split()
# number_of_students = len(student_heights)
# total = 0
# for height in student_heights:
#     total += int(height)
#
# average_height = int(total/number_of_students)
#
# print(average_height)

# # Student score
# student_score = input().split()
# for n in range(0, len(student_score)):
#     student_score[n] = int(student_score[n])
#
# temp = 0
# for score in student_score:
#     if int(score) > temp:
#         temp = score
#
# print(temp)

# # Create a Program to sum up all the numbers from 1 to 100
# total = 0
# for number in range(1,101):
#     total += number
#
# print(total)


# # Create a Program to add all the even number between 1 to 100
#
# total = 0
# range_value = int(input("What was the ending number?\n"))
# for number in range(1, range_value + 1):
#     if number % 2 == 0:
#         total += number
#
# print(total)

# # Create a Fizz Buzz Program
#
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

