# Fibonacci numbers

while True:
  user_input = input('How many steps do you want for create fibonacci series?:> ')
  if user_input == 'exit':
      print('You are quitting from the fibonacci numbers program...')
      break
  else:
      try:
        a = 0
        b = 1
        user_input = int(user_input)
        fibonaccinumlist = []
        if user_input == 0 or user_input < 0:
            print('Please enter a positive number')
        else:
            for i in range(user_input):
                fibonaccinumlist.append(a)
                a, b = b, a + b
            print(f'For first {user_input} step, fibonacci numbers are: {fibonaccinumlist}')
      except ValueError:
          print('Please provide a valid number.')
