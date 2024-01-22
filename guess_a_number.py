import random

computer_move = random.randint(1, 100)
attempts = 0
while True:
    player_input = input("Guess the number (1-100): ")
    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue

    player_number = int(player_input)
    if player_number == computer_move and attempts < 10:
        print("You guess it!")
        break
    elif player_number > computer_move and attempts < 10:
        print("Too High!")
        attempts += 1
    else:
        if attempts < 10:
            print("Too Low!")
        attempts += 1
    if attempts > 10:
        print("No more attempts left!")
        break
