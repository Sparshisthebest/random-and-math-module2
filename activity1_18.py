import random
playing=True
number=str(random.randint(10,20))
print("i will generate a number from 0-9, and you have to guess the number 1 digit at a time")
print("the game ends when you get one")
while playing:
    guess=input("give me your best guess \n")
    if number==guess:
        print("you win the game ")
        print("the number was ",number)
        break
    else:
        print("your guess is not quite right try again thats a massivie skill issue")
