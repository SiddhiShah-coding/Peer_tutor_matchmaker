
import random

number = random.randint(10, 50)
ctr = 0
while ctr < 5:
    guess = int(input("Guess a number in range 10-50:"))
    if guess == number:
        print("You win")
        break
    else:
        ctr += 1
if not ctr < 5:
    print("YOU LOSE \n the number was", number)