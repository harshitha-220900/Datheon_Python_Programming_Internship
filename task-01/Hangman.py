import random
from hangman_stages import stages
import os

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "words.txt"
)

with open(file_path, "r") as file:
    my_list = file.read().splitlines()
chosen_word=random.choice(my_list).lower()

lives=6
placeholder=""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)
correct_letters=[]
game_over=False
while not game_over:
    guess=input("Guess a letter: ").lower()

    #to check the guessed letter is in the word
    display=""
    hangman=[]
    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        elif letter in correct_letters:
            print("You have already guessed this letter")
        else:
            display += "_"
    print(display)
    if guess not in chosen_word:
        print(stages[lives])
        print("the letter is not in the word")
        lives -=1

    if "_" not in display:
        game_over=True
        print("You win!")
    else:
        if lives < 0:
            print(f"The word is {chosen_word}")
            print("You lose!")
            game_over=True