#!/usr/bin/python3
import random
n = random.randint(-10000, 10000)
ld = n % 10
if n < 0:
    n = n * -1
    ld = n % 10
    ld *= -1
    n *= -1
if lastdigit > 5:
    print("Last digit of {} is {} and is greater than 5".format(n, ld))
if ld == 0:
    print("Last digit of {} is {} and is 0".format(n, ld))
if ld < 6 and ld != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(n, ld))
