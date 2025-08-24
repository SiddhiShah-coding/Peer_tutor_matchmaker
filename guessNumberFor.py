
import random

number = random.randint(10, 50)

for i in range(0,5):
    guess = int(input("Guess a number in range 10-50:"))
    if guess == number:
        print("You win")
        break
    elif i==4 :
        print("YOU LOSE \n the number was", number)
