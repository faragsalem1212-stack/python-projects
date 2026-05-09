hangman_ascii = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]
import random

# computer_word

words = ["bird", "car", "fans", "room", "shirt", "billow"]
com_word = random.choice(words)

# the interface

print("Welcome to guess the word game!")
display = ["_"] * len(com_word)
the_word_in_letters = []
for x in com_word:
    the_word_in_letters += x
print(" ".join(display))
print(hangman_ascii[0])

lives = 6
guessed_letters = []

while "_" in display and lives > 0:
    letter = input("guess a letter: ")
    
    # checking
    
    if letter in guessed_letters:
        print("you guessed this one, guess another letter: ")
        continue
        
    else:
        guessed_letters.append(letter)

        # right guess
        if letter in the_word_in_letters:
            print("right!!!")
            for x in range(len(the_word_in_letters)):
                if the_word_in_letters[x] == letter:
                    display[x] = letter
            print(" ".join(display))
        else:
            # wrong guess
            lives -= 1
            print(f"wrong, you have {lives} lives left.")
            print(hangman_ascii[6 - lives])
# finishing
if lives == 0:
    print("you lost!!!")
    print(f"the word was {com_word}")
else:
    print(com_word)
    print("You Wooon!")
