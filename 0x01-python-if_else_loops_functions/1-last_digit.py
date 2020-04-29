#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = number % 10
if number < 0:
    number = number * -1
    lastdigit = number % 10
    lastdigit *= -1
    number *= -1
if lastdigit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lastdigit))
if lastdigit == 0:
    print("Last digit of {} is {} and is 0".format(number, lastdigit))
if lastdigit < 6 and lastdigit != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, lastdigit))

