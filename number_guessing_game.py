# Guess the number games

print("*=* Number Guessing Game *=*")

number = 91

guess_left = 1

print("\nGuess a number between 1 - 100")

print("\nTotal number of guesses are 5.")

while guess_left<=10:
    guess_number = int(input("\nGuess number: "))
    if 100 > guess_number > 91:
        print("\nYou guess bigger than actual number. ")
    elif guess_number < 91:
        print("\nYou guess smaller than actual number.")
    elif guess_number > 100:
        print("\nInvalid Input. Guess number between 1 and 100.")
    else:
        print("\n\tCongrats, You guess correct number. YOU WON..!")
        break
    print(f'{10-guess_left}, guesses left.')
    guess_left = guess_left + 1


if guess_left > 10:
    print("\n\n\t\t\t\tSORRY ... YOU LOSE")

