#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    lastdg = int(str(number)[-1])
elif number < 0:
    lastdg = int(str(number)[-1]) * -1
else:
    lastdg = 0
if lastdg > 5:
    print(f"Last digit of {number} is {lastdg} and is greater than 5")
elif lastdg < 6 and lastdg != 0:
    print(f"Last digit of {number} is {lastdg} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {lastdg} and is 0")
