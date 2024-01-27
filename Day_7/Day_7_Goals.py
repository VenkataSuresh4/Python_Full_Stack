import random
import Day_7_Hangman_art
import Day_7_Hangman_words

# Print the Hangman logo
print(Day_7_Hangman_art.logo)

# Guess a Random Word from the llist
words = Day_7_Hangman_words.word_list
chosen_word = random.choice(words).lower()

print(chosen_word)
# Create the required variables
display_word = []
end_of_game = False
lives = 6

for blank in chosen_word:
    display_word.append("_")

while not end_of_game:
    guess_word = input("Guess a Word: ").lower()

    if guess_word in display_word:
        print("You have already guessed the word!!")
    elif guess_word in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess_word:
                display_word[position] = guess_word
        print(display_word)
    else:
        lives -= 1
        print(Day_7_Hangman_art.stages[lives])
        print(f"You left with {lives} lives")

    if lives == 0:
        print("You Loose! Person Dead")
        end_of_game = True

    if "_" not in display_word:
        print("You Win")
        end_of_game = True
