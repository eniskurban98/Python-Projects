'''
Question:
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''

user_input = int(input('Enter a number between 1 and 12:> '))
times = 0

if (user_input < 1 or user_input > 12):
    print('Please enter the number in range. Let\'s try again!')
    user_input = int(input('Enter a number between 1 and 12:> '))

for i in range(1,12+1):
    times = i * user_input
  # print(times)
    print('{} * {} = {}'.format(i,user_input,i*user_input))
