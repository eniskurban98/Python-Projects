'''
Question :
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.
'''

user_input1 = int(input("Please enter a number between 1 and 100:> "))
user_input2 = int(input("Please enter another number between 1 and 100:> "))

list = []

while ((user_input1 < 1 and user_input2 < 1) or (user_input1 > 100 and user_input2 > 100)):
    print('Numbers must be different values between 1 and 100, let us try again')
    user_input1 = int(input('Please enter a number between 1 and 100:> '))
    user_input2 = int(input('Please enter another number between 1 and 100:> '))

if (user_input1 == user_input2):
    print('There is nothing to count')
elif (user_input1 < user_input2):
    for i in range(user_input1,user_input2+1):
        list.append(i)
        print(i, end = ' ')
        if (i % 20 == 0):
            print('\n')
    print(list)
elif (user_input2 < user_input1):
    for i in range(user_input2, user_input1+1):
        list.append(i)
        print(i, end = ' ')
        if (i % 20 == 0):
            print('\n')
    print(list)
else:
    print('Unknown enter')

