from math import *
from random import *

x = int(input("Enter the number to find the square root :"))
print("Square :", sqrt(x))

first = int(input("Enter two numbers find GCD :"))
second = int(input())
print("gcd =", gcd(first, second))

degree = int(input("Enter the degree to find trigonometric functions :"))
print("cos :", cos(degree), "sin :", sin(degree), "tan :", tan(degree))

first = int(input("Enter two number to generate random number :"))
second = int(input())
print(randrange(first, second))
