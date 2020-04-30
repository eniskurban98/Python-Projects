# A factorial program with unending loop, that asks user input permanently until user quits from the program.

while True:
    user_input = input("Enter a number:> ")
    if user_input == "exit":
        print('You are quitting the program...')
        break
    else:
        try:
            factorial = 1
            user_input = int(user_input)
            if user_input < 0:
                print("Sorry, factorial does not exist for negative numbers.")
            elif user_input == 0:
                print("The factorial of 0 is 1.")
            else:
                for i in range(1, user_input + 1):
                    factorial = factorial * i
                print(f'The factorial of {user_input} is {factorial}.')
        except ValueError:
            print("Please provide a valid number")
