name = input("your name:")
print("hi:",name)
age = int(input("how old are you:"))
if age >= 18:
    print(" you have")
else:
    print("no")
answer = input("DO YOU WANT PLAY A game,(yes/no):")
if answer == "yes":
    print("lets go")
else:
    print("oh ok")
print("GUES THE NUMBER")

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
        print("you won")
        break
    print("you have",tries,"tries")
if tries == 0:
    print("you lose number was:", number)
print("again")

import random
number = random.randint(1,100)
tries = 10
print("you have 10 tries")
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


import random
print("you have 10 tries")
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

import random
tries = 10
print("you have 10 tries")
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

    
