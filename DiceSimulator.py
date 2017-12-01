#Dice Rolling Simulator
import random


def main():
    print(random.randint(1, 6))
    again = input("Would you like to run it again? [Y/N]")
    if again == 'Y':
        main()
    else:
        print("Thank you for playing")

print("This simulator will give you a random number from 1-6")
Roll = str.lower(input("Please say 'Roll' to roll the dice: "))
if Roll == 'roll':
    main()

    
    
    
