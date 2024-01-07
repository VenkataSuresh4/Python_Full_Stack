# Random Module
import random

random_integer = random.randint(0, 100)
print(random_integer)

# Heads[1] or Tail[0]
random_value = random.randint(0, 1)
if random_value == 1:
    print("Heads")
else:
    print("Tails")

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii", "Visakhapatnam"]

# Functions for List - append, extend, insert, remove, count, sort, reverse, copy,
# append
print(states_of_america[-1])

# extend
states_of_america.extend(["'Vizag','Anakapalle','Duvvada' "])
print(states_of_america)

# insert
states_of_america.insert(-1, "Attili")
print(states_of_america[-1])

# Who will pay the bill - Banker Roulette
text = input()
names = text.split(',')
print(random.choice(names))
