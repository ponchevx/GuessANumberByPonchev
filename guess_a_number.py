import random

computer_move = random.randint(1, 100)
level_2_activated = False
attempts = 0

while True:
    player_input = input("Guess the number (1-100): ")
    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue

    player_number = int(player_input)
    if player_number == computer_move and attempts < 10:
        level_2_activated = True
        print("You guess it!")
        break
    elif player_number > computer_move and attempts < 10:
        print("Too High!")
        attempts += 1
    else:
        if attempts < 10:
            print("Too Low!")
        attempts += 1
    if attempts == 10 and player_number != computer_move:
        print("No more attempts left!")
        break

if level_2_activated:
    print("Level 2 of the game begins!")
computer_move_2 = random.randint(1, 200)
attempts_2 = 0

while level_2_activated:
    player_input = input("Guess the number (1-200): ")
    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue

    player_number = int(player_input)
    if player_number == computer_move_2 and attempts_2 < 20:
        level_2_activated = True
        print("You guess it and have beaten the game! Congratulations!")
        break
    elif player_number > computer_move_2 and attempts_2 < 20:
        print("Too High!")
        attempts_2 += 1
    else:
        if attempts_2 < 20:
            print("Too Low!")
        attempts_2 += 1
    if attempts_2 == 20 and player_number != computer_move_2:
        print("No more attempts left!")
        break