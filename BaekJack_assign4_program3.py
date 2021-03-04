"""
Assignment #4, Question 3
Jack Baek
"""

#creating input function for user to input throws
throws = int(input("Number of throws: "))

while throws <= 0:#creating while loop to force user to input valid number
    print("Invalid, number of throws. Try again!")
    print()
    throws = int(input("Number of throws: "))

var = throws

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
lgrey = 0
misses = throws

#
while throws != 0:
    x = random.uniform(0,800)
    y = random.uniform(0,500)
    if 400 <= x <= 450 and 50 <= y <= 200: #red rectangle
        red += 1
        misses -= 1
        throws -= 1
    if 50 <= x <= 250 and 50 <= y <= 450: #green rectangle
        green += 1
        misses -= 1
        throws -= 1
        if 100 <= x <= 150 and 100 <= y <= 150:
            green -= 1
            misses += 1
        if 150 <= x <= 200 and 200 <= y <= 250:
            green -= 1
            misses += 1
        if 100 <= x <= 200 and 300 <= y <= 400:
            green -= 1
            misses += 1
    if 350 <= x <= 550 and 250 <= y <= 450:
        blue += 1
        misses -= 1
        throws -= 1
        if math.sqrt((x-450)**2+(y-350)**2) > 100:
            blue -= 1
            misses += 1
    if 550 <= x <= 750 and 100 <= y <= 300: #for bigger circle
        greybig += 1
        throws -= 1
        misses -= 1
        if math.sqrt((x-650)**2+(y-250)**2) > 100:
            greybig -= 1
            misses += 1
    if 600 <= x <= 700 and 250 <= y <= 350: #for smaller circle
        greysmall += 1
        misses -= 1
        throws -= 1
        if math.sqrt((x-650)**2+(y-300)**2) > 50: #outside the circle
            greysmall -= 1
            misses += 1
        if 600 <= x <= 700 and 250 <= y <= 300:
            greysmall -= 1
            lgrey += 1
            misses -= 1
            if math.sqrt((x-650)**2+(y-300)**2) > 50:
                lgrey -= 1
                misses += 1
end = time.time()

dgrey = greybig + greysmall 

#creating print header
print()
print("Total time elapsed :", end-start, "seconds")
print()

print("Red:", format(red,'>20,'), " (", format(red/var*100,'.2f'), "%)", sep = "")
print("Blue:", format(blue,'>19,'), " (", format(blue/var*100,'.2f'), "%)", sep = "")
print("Green:", format(green,'>18,'), " (", format(green/var*100,'.2f'), "%)", sep = "")
print("Dark Grey:", format(dgrey,'>14,'), " (", format(dgrey/var*100,'.2f'), "%)", sep = "")
print("Light Grey:", format(lgrey,'>13,'), " (", format(lgrey/var*100,'.2f'), "%)", sep = "")
print("Misses:", format(misses,'>17,'), " (", format(misses/var*100,'.2f'), "%)", sep = "")

