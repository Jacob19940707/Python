#Guess that Number Game
import random
Guess = True
rand = random.randint(1, 10)
print("Guess an integer from 1-10! Have Fun!")

def main():
    global Guess
    
    user = int(input("Enter what number you think it is: "))
    if user > rand:
        print("Your number was higher than the number! Guess again!")
    elif user < rand:
        print("Your number was lower than the number! Guess again!")
    elif user == rand:
        print("Good job you guessed correctly!")
        again = input("Do you want to play again? Y/N: ")
        if again == 'Y':
            print("Okay, let's play again!")
        else:
            
            print("Thank you for playing!")
            Guess = False;
            

while Guess == True:
    main()
        
       



