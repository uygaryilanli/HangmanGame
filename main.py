import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

while True:
    print(logo)
    print("***************Welcome to Hangman***************")
    gameChooser = int(input("1-Play Game\n2-Exit Game\nYour Choice: "))
    
    if gameChooser == 1:
        chosen_word = random.choice(word_list)
        word_length = len(chosen_word)
        lives = 6
        display = ["_" for _ in range(word_length)]

        while True:
            guess = input("Guess a letter: ").lower()

            if guess in display:
                print(f"You've already guessed {guess}")

            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter

            if guess not in chosen_word:
                lives -= 1
                print(stages[lives])
                print(f"Your health is {lives}")
                if lives == 0:
                    print("You lose.")
                    print(f"Truth answer is {chosen_word}")
                    break

            if "_" not in display:
                print("You win.")
                break

            print(" ".join(display))
    elif gameChooser == 2:
        print("You are leaving the game...")
        break
    else:
        print("Please choose 1 or 2")