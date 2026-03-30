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
print("GUES THE NUMBER")

print("EASY ROUND")
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
        break
    print("you have",tries,"tries")
if tries == 0:
    print("you lose number was:", number)
print("again")

print("MIDLE MEDIUM ROUND")
print("NEXT GAME")
import random
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
        print("you won")
        break
    print("you have",tries,"tries")
if tries == 0:
    print("you lose number was:", number)
    tries = 10


print("MEDIUM ROUND")
print("NEXT GAME")
import random
number = random.randint(1,300)
print("you have 10 tries")
print("number is 1,300")
while tries > 0:
    guess = int(input("your turn:"))
    tries -= 1
    if guess > number:
        print("big")
    elif guess < number:
        print("small")
    else:
        print("you won")
        break
    print("you have",tries,"tries")
if tries == 0:
    print("you lose number was:", number)


print("HARD ROUND!")
print("NEXT GAME")
import random
number = random.randint(1,1000)
tries = 10
print("you have 10 tries")
print("number is 1,1000")
while tries > 0:
    guess = int(input("your turn:"))
    tries -= 1
    if guess > number:
        print("BIG")
    elif guess < number:
        print("SMALL")
    else:
        print("YOU WON",name)
        break
    print("YOU HAVE",tries,"TRIES")
if tries == 0:
    print("you lose number was:", number)


print("!!!!EXTREME ROUND!!!!")
 print("NEXT GAME")
import random
tries = 10
print("you have 10 tries")
number = random.randint(1,1500)
print("number is 1,5000")
while tries > 0:
    guess = int(input("your turn:"))
    tries -= 1
    if guess > number:
        print("BIG")
    elif guess < number:
        print("SMALL")
    else:
        print("YOU WON",name)
        break
    print("you have",tries,"tries")
if tries == 0:
    print("you lose number was:", number)
print("GAMES END, NEW GAMES BE SOON")
print("BYE",name)
