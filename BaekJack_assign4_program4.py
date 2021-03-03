"""
Assignment #4, Question 4
Jack Baek
"""
#asking user for number 
number = int(input("Enter a number greater than or equal to 0: "))

#creating a while loop to ensure number is valid 
while number < 0:
    print("Invalid, try again")
    print()
    number = int(input("Enter a number greater than or equal to 0: "))

#setting binary variable to a string so it can be added 
binary = ""

#creating if state for when number is 0
if number == 0:
    binary = "0"

#creating while loop for when number is not 0 
while number != 0:
    re = str(number%2)
    binary = re + binary
    print(number, "% 2 =", (number%2), "---", binary)
    print(number, "/ 2 =", (number//2))
    number //= 2 

#print function 
print()
print(number, "in binary is", binary)
