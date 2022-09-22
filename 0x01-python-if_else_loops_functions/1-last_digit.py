#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number *= -1
the_number = (number % 10)
print(f"Last digit of {number} is {the_number}", end="")
if the_number > 5:
    print(" and is greater than 5")
elif the_number== 0:
    print(" and is 0")
elif the_number  < 6 and the_number != 0:
    print(" and is less than 6 and not 0")
