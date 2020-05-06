# Simple calculator

while True:
    print("Options: \n")
    print("Enter 'add' to add two numbers ")
    print("Enter 'substract' to substract two numbers ")
    print("Enter 'multiply' to multiply two numbers ")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")
    user_input = input(": ")

    if (user_input == "quit"):
        print("You quitted from the calculating program successfully!")
        break

    elif (user_input == "add"):
        a = float(input("Enter a number: "))
        b = float(input("Enter another number: "))
        result = print("Result: ",str(a+b))
        print("\n")

    elif (user_input == "substract"):
        a = float(input("Enter a number: "))
        b = float(input("Enter another number: "))
        result = print("Result: ",str(a-b))
        print("\n")

    elif (user_input == "multiply"):
        a = float(input("Enter a number: "))
        b = float(input("Enter another number: "))
        result = print("Result: ",str(a*b))
        print("\n")

    elif (user_input == "divide"):
        a = float(input("Enter a number:"))
        b = float(input("Enter another number: "))
        result = print("Result: ",str(a/b))
        print("\n")

    else:
        print("Unknown input")
        print("\n")