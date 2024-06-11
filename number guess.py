import random

guess_taken=0

print("Hi friend what is your name?")
name =  input()

num = random.randint(0,40)

guess = int(input(name + " I am thinking of a number between 1 and 40 can you guess what it is ?"))

while guess_taken < 4:
    guess_taken = guess_taken + 1
    if guess < num:
        print("you need to guess higher...Try again!")
        guess = int(input("guess a number between 1 and 40:"))
    else:
         print("you need to guess lower...Try again!")  
         guess = int(input("guess a number between 1 and 40:"))               

    if guess==num:
       break

if guess==num:
    guess_taken = str(guess_taken)
    print("Good job!"+ name + " you guessed my number in "+ guess_taken + " guessed")

if guess!=num:
    num = str(num)
    print("Nobe! , the number I was Think is ",num)