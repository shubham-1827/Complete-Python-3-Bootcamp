# number guessing game

from random import randint

want_to_play = True
while want_to_play:

    secret_number = randint(1, 100)

    number_found = False
    guesses = [0]
    while not number_found:
        guess_number = int(input("Guess a number between 1 to 100 : "))
        if guess_number <= 0 or guess_number > 100:
            print("Out Of Bounds???")
            continue
        if guess_number == secret_number:
            print(
                f"Yooo, You find the number {secret_number} after {len(guesses)} guesses!!!"
            )
            break

        guesses.append(guess_number)

        if guesses[-2]:
            if abs(guess_number - secret_number) < abs(secret_number - guesses[-2]):
                print("WARMER!!!!!")
            else:
                print("COLDER!!!!!")
        elif abs(guess_number - secret_number) <= 10:
            print("WARM!!!!!")
        else:
            print("COLD!!!!!")

    play_more = input("Want to play more : (Y or N) : ")
    if play_more == "n":
        want_to_play = False
