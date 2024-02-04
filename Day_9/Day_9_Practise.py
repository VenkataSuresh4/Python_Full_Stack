# programming = {
#     "Bug": "Be Careful before we raise it",
#     "Error": "Error in Code"
# }

# print(programming["Bug"])
#
# programming["Bug"] = "How do we identify the bug"
#
# print(programming["Bug"])
#
# programming = {}
#
# print(programming)
#
# programming["Looping"] = "Iterates until the given number"
#
# print(programming)

# # Loop Through the dictionary
#
# for thing in programming:
#     print(programming[thing])

# # Write a program for Grading
# # 91 - 100 - "Outstanding"
# # 81 - 90 - "Exceeds Expectation"
# # 71 -80 - "Acceptable"
# # 70 or < 70 - "Fail"
#
# student_grades = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62
# }
#
# for student in student_grades:
#     score = student_grades[student]
#
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectation"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
#
# print(student_grades)

# # Nesting
# # List inside Dictionary
#
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }
#
# # Dictionary inside another Dictionary
#
# travel_log_2 = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Dijon"]
#     },
#     "Germany":{
#         "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"]
#     }
# }
#
# print(travel_log_2["France"]["cities_visited"])

# # Dictionary in List
#
# travel_log_2 = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5
#     }
# ]
#
# print(travel_log_3[0]["country"])

country = input()
visits = int(input())
list_of_cities = eval(input())

travel_log_2 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
]


def add_new_country(name, times, places):
    travel_log_2.append({
        "country": name,
        "total_visits": times,
        "cities_visited": places
    })

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log_2[2]['country']} {travel_log_2[2]['total_visits']} times.")
print(f"My favorite city was {travel_log_2[2]['cities_visited'][0]}.")