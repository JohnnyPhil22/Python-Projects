import random
import math

lower_limit = int(input("Enter Lower Limit Number:- "))
upper_limit = int(input("Enter Upper Limit Number:- "))

x = random.randint(lower_limit, upper_limit)
print("\n\tYou've only ",round(math.log(upper_limit - lower_limit + 1, 2))," chances to guess the integer!\n")

count = 0

while count < math.log(upper_limit - lower_limit + 1, 2):
    count += 1
    guess = int(input("Guess a number:- "))
    if x == guess and count == 1:
        print("Congratulations! You did it in 1 try!")
        break
    if x == guess and count > 1:
        print("Congratulations! You did it in ",count," tries!")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

if count >= math.log(upper_limit - lower_limit + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
