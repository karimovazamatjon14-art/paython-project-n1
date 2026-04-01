name = input("your name:")
print("HI:",name)

age = int(input("how old are you:"))
if age >= 18:
    print("OK")
else:
    print("NO")
    answer = input("DO YOU WANT PLAY A game,(yes/no):")
if answer == "yes":
    print("LETS PLAY:",name)
else:
    print("OH OK BUT YOU WILL:)")
Azamat_game_points = 0
print("GUES THE NUMBER")
print("you shold guess the number")
print("at start you have 10 tries on 1 game")
print("the game has modes ")
print("c,b,a,s,ss and sss+")
print("        .")
print("        .")
print("         .")
print("      .")
print("         .")
print("       .")
print("         .")

print("EASY ROUND")
print("C")
print("WIN TO TAKE 3 Azamat_game_points")
import random
print("                          ")
number = random.randint(1,50)
tries = 10
print("you have 10 tries")
print("number is 1,50")
while tries > 0:
    guess = int(input("your turn:"))
    tries -= 1
    if guess > number:
        print("big")
    elif guess < number:
        print("small")
    else:
        print("you won:",name)
        Azamat_game_points += 3
        break
    print("you have",tries,"tries")
if tries == 0:
    print("you lose number was:", number)
print("again")




print("MIDLE MEDIUM ROUND")
print("C+")
print("WIN TO TAKE 6 Azamat_game_points")
import random
print("                          ")
number = random.randint(1,100)
tries = 10
print("you have 10 tries")
print("number is 1,100")
while tries > 0:
    guess = int(input("your turn:"))
    tries -= 1
    if guess > number:
        print("big")
    elif guess < number:
        print("small")
    else:
        print("you won:",name)
        Azamat_game_points += 6
        break
    print("you have",tries,"tries")
if tries == 0:
    print("you lose number was:", number)
print("again")


print(" MEDIUM ROUND")
print("B")
print("WIN TO TAKE 10 Azamat_game_points")
import random
print("                          ")
number = random.randint(1,500)
tries = 10
print("you have 10 tries")
print("number is 1,500")
while tries > 0:
    guess = int(input("your turn:"))
    tries -= 1
    if guess > number:
        print("big")
    elif guess < number:
        print("small")
    else:
        print("you won:",name)
        Azamat_game_points += 10
        break
    print("you have",tries,"tries")
if tries == 0:
    print("you lose number was:", number)
print("again")



print("!HARD ROUND!")
print("A")
print("WIN TO TAKE 3=15 Azamat_game_points")
import random
print("                          ")
number = random.randint(1,1000)
tries = 10
print("you have 10 tries")
print("number is 1,1000")
while tries > 0:
    guess = int(input("your turn:"))
    tries -= 1
    if guess > number:
        print("big")
    elif guess < number:
        print("small")
    else:
        print("you won:",name)
        Azamat_game_points += 15
        break
    print("you have",tries,"tries")
if tries == 0:
    print("you lose number was:", number)
print("again")


print("!!SUPER HARD ROUND!!")
print("S")
print("WIN TO TAKE 18 Azamat_game_points")
import random
print("                          ")
number = random.randint(1,2000)
tries = 10
print("you have 10 tries")
print("number is 1,2000")
while tries > 0:
    guess = int(input("your turn:"))
    tries -= 1
    if guess > number:
        print("big")
    elif guess < number:
        print("small")
    else:
        print("you won:",name)
        Azamat_game_points += 18
        break
    print("you have",tries,"tries")
if tries == 0:
    print("you lose number was:", number)
print("again")




print("!!!EXTREME ROUND!!!")
print("SS")
print("WIN TO TAKE 35 Azamat_game_points")
import random
print("                          ")
number = random.randint(1,5000)
tries = 10
print("you have 10 tries")
print("number is 1,5000")
while tries > 0:
    guess = int(input("your turn:"))
    tries -= 1
    if guess > number:
        print("big")
    elif guess < number:
        print("small")
    else:
        print("you won:",name)
        Azamat_game_points += 35
        break
    print("you have",tries,"tries")
if tries == 0:
    print("you lose number was:", number)
print("again")






print("!!!INPOSSIBLE ROUND!!!")
print("SS+")
print("WIN TO TAKE 100 Azamat_game_points")
import random
print("                          ")
number = random.randint(1,100000)
tries = 10
print("you have 10 tries")
print("number is 1,100000")
while tries > 0:
    guess = int(input("your turn:"))
    tries -= 1
    if guess > number:
        print("big")
    elif guess < number:
        print("small")
    else:
        print("you won:",name)
        Azamat_game_points += 100
        break
    print("you have",tries,"tries")
if tries == 0:
    print("you lose number was:", number)
print("again")

print("!!!NEW GAME!!!")

tries = 5
stage = 1
print("YOU HAVE 50% CHANSE TO CHOOSE CORRECT NUMBER")
print("!!!THE GAME HAS 50 STAGES!!!")
print("WIN TO GET 200 Azamat_game_points")
while tries > 0:
    import random
    number = random.randint(1,2)
    n = int(input("1 or 2:"))
    if n == number:
        print("!!!!!!!GREAT!!!!!!")
        
    else:
        print("!!!!NOOOOOOO!!!!")
        tries -= 1
    stage += 1
    print("YOU ARE ON",stage,"STAGE")
    print("YOU HAVE",tries,"TRIES")
if tries == 0:
    print("GAME OVER YOU WAS ON",stage,"STAGE")
if stage == 50:
    print("you won")
    Azamat_game_points += 200
   













print("GAMES END, NEW GAMES BE SOON")
print("BYE",name)









