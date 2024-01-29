import random
import sys
print("Enter a range")
x = int(input("\nLower:"))
y = int(input("\nUpper:"))

pythonnum = random.randint(a=x, b=y)

guess = int(input("\nGuess the number in the selected range:"))
        
if pythonnum == guess:
    print("You guessed the correct number")
else:
    print("Incorrect")