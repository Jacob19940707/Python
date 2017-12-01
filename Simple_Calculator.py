#SimpleCalculator
def main():
    print("Please add spaces between each item")
    User_Input = input("Please enter your function to be calculated: ")
    User_Input = User_Input.split()



    if User_Input[1] == '+':
        Calculate = float(User_Input[0]) + float(User_Input[2])
        print(Calculate);
    elif User_Input[1] == '-':
        Calculate = float(User_Input[0]) - float(User_Input[2])
        print(Calculate);
    elif User_Input[1] == '*':
        Calculate = float(User_Input[0]) * float(User_Input[2])
        print(Calculate);
    elif User_Input[1] == '/':
        Calculate = float(User_Input[0]) / float(User_Input[2])
        print(Calculate);
    else:
        print("Please enter one of the following operators: +, -, *, /")
        main()

    A1 = input("Do you want to calculate something else? [Y/N] ")


    if A1 == 'Y':
        main()
    else:
        print("Thank you!")

main()
    
        

    
