# goal of this code is to
# make a function in which the user can define the range of numbers that the computer can choose a random number from
# a while loop where the user inputs a number, ccode checks to see if its the right number, if it is say "yay" or something simaler, if not continue the loop
import random


def randNumbRangePicker(range):  # picks a random number from range (+1 to skip over 0)
    RAND = random.SystemRandom()
    return ((RAND.random() * range).__int__()) + 1


tries = int(input("Enter how many tries to get the number: "))
rang = int(input("Enter the max range that the computer can draw from: "))
number = randNumbRangePicker(rang)

for X in range(tries):  # the guessing section
    guess = int(input(f"number of tries left: {tries - X}\nWhat is your guess from 1 - {rang}?:"))
    if guess == number:
        break
    else:
        print(f"{guess} is incorrect")

print(f"THAT'S CORRECT!!\n{guess} is the correct guess!!")
