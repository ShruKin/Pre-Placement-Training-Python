# 4. Check whether the given number is a Krishnamurti number or not

from math import factorial

num = input("Enter a number: ")

if int(num) == sum([factorial(int(x)) for x in num]):
    print(num, "is a Krishnamurti number")
else:
    print(num, "is a not Krishnamurti number")
