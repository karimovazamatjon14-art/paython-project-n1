import random

name = input("your name: ")
print("HI:", name)

age = int(input("how old are you: "))
if age >= 18:
    print("OK")
else:
    print("NO")
    answer = input("DO YOU WANT PLAY A game (yes/no): ")
    if answer != "yes":
        print("OH OK BUT YOU WILL :)")
        exit()

Azamat_game_points = 0


def play_again():
    while True:
        choice = input("1 - replay, 2 - menu: ")
        if choice == "1":
            return True
        elif choice == "2":
            return False


def guess_game(max_number, points):
    global Azamat_game_points

    number = random.randint(1, max_number)
    tries = 10

    print(f"number is 1-{max_number}")
    print("you have 10 tries")

    while tries > 0:
        guess = int(input("your turn: "))
        tries -= 1

        if guess > number:
            print("big")
        elif guess < number:
            print("small")
        else:
            print("you won:", name)
            Azamat_game_points += points
            return

        print("you have", tries, "tries")

    print("you lose, number was:", number)


def game8():
    global Azamat_game_points

    tries = 5
    stage = 1

    print("YOU HAVE 50% CHANCE")
    print("50 STAGES")

    while tries > 0 and stage <= 50:
        number = random.randint(1, 2)
        n = int(input("1 or 2: "))

        if n == number:
            print("GREAT")
        else:
            print("WRONG")
            tries -= 1

        stage += 1
        print("stage:", stage)
        print("tries:", tries)

    if stage > 50:
        print("YOU WON!")
        Azamat_game_points += 200
    else:
        print("GAME OVER")


while True:
    print("\n----MENU----")
    print("1 - EASY (1-50)")
    print("2 - MEDIUM (1-100)")
    print("3 - HARD (1-500)")
    print("4 - VERY HARD (1-1000)")
    print("5 - SUPER HARD (1-2000)")
    print("6 - EXTREME (1-5000)")
    print("7 - IMPOSSIBLE (1-100000)")
    print("8 - SPECIAL GAME")
    print("0 - EXIT")

    choice = input("choose: ")

    if choice == "1":
        while True:
            guess_game(50, 3)
            if not play_again():
                break

    elif choice == "2":
        while True:
            guess_game(100, 6)
            if not play_again():
                break

    elif choice == "3":
        while True:
            guess_game(500, 10)
            if not play_again():
                break

    elif choice == "4":
        while True:
            guess_game(1000, 15)
            if not play_again():
                break

    elif choice == "5":
        while True:
            guess_game(2000, 18)
            if not play_again():
                break

    elif choice == "6":
        while True:
            guess_game(5000, 35)
            if not play_again():
                break

    elif choice == "7":
        while True:
            guess_game(100000, 100)
            if not play_again():
                break

    elif choice == "8":
        while True:
            game8()
            if not play_again():
                break

    elif choice == "0":
        print("BYE")
        break


