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
print("C")
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
print("C+")
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
        break
    print("you have",tries,"tries")
if tries == 0:
    print("you lose number was:", number)
print("again")



print(" MEDIUM ROUND")
print("B")
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
        break
    print("you have",tries,"tries")
if tries == 0:
    print("you lose number was:", number)
print("again")



print("!HARD ROUND!")
print("A")

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
        break
    print("you have",tries,"tries")
if tries == 0:
    print("you lose number was:", number)
print("again")


print("!!SUPER HARD ROUND!!")
print("S")

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
        break
    print("you have",tries,"tries")
if tries == 0:
    print("you lose number was:", number)
print("again")




print("!!!EXTREME ROUND!!!")
print("SS")

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
        break
    print("you have",tries,"tries")
if tries == 0:
    print("you lose number was:", number)
print("again")






print("!!!INPOSSIBLE ROUND!!!")
print("SS+")

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
        break
    print("you have",tries,"tries")
if tries == 0:
    print("you lose number was:", number)
print("again")



print("GAMES END, NEW GAMES BE SOON")
print("BYE",name)
