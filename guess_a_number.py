import random

computer_move = random.randint(1, 100)
while True:
    player_input = input("Guess the number (1-100): ")
    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue

    player_number = int(player_input)
    if player_number == computer_move:
        print("You guess it!")
        break
    elif player_number > computer_move:
        print("Too High!")
    else:
        print("Too Low!")
