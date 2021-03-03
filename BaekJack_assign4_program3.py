"""
Assignment #4, Question 3
Jack Baek
"""

#creating input function for user to input throws
throws = int(input("Number of throws: "))

while throws < 0:#creating while loop to force user to input valid number
    print("Invalid, number of throws. Try again!")
    print()
    throws = int(input("Number of throws: "))

import time

#creating print header
print()
print("Total time elapsed :", time.time(), "seconds")
print()

import random
import math

#counter for each shape
red = 0
green = 0
blue = 0
greysmall = 0
greybig = 0

#
while throws != 0:
    x = random.uniform(0,800)
    y = random.uniform(0,500)
    if x == [(400, 450)] and y == [(50, 200)]:
        red += 1
        throws -= 1
    if x == [50, 250] and y == [50, 400]:
        green += 1
        throws -= 1

print("Red:", format(red,'>12, .2f'), )       
    

