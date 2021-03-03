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
start = time.time()


import random
import math

#counter for each shape
red = 0
green = 0
blue = 0
greysmall = 0
greybig = 0
misses = 0

#
while throws != 0:
    x = random.uniform(0,800)
    y = random.uniform(0,500)
    if 400 < x < 450 and 50 < y < 200:
        red += 1 
        throws -= 1
    if 50 < x < 250 and 50 < y < 400:
        green += 1
        throws -= 1
        if x == 150 and y == 150:
            green -= 1
            misses += 1
        if x == 600 and y == 250:
            green -= 1
            misses += 1
        if 100 < x < 200 and 300 < y < 400:
            green -= 1
            misses += 1
    if 350 < x < 500 and 250 < y < 450:
        blue += 1
        throws -= 1

end = time.time()

#creating print header
print()
print("Total time elapsed :", end-start, "seconds")
print()
print("Red:", red)
print ("Green:", green)
print("Blue:", blue)
print ("Misses:", misses)



