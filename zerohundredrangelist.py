# Find the numbers between 0-100 with step 5, in every step include the new number on the list that we
# created, print how many numbers on the list and print the sum of numbers.


count = 0
sum = 0
list = []

for i in range(0,100,5): # loop for our numbers
    list.append(i)   # We create our list here.
    print(i)
    print(list)
    sum = sum + i
    count = count + 1 # this part shows how many elements on the list
print("Numbers of the list:",count)
print("Sum of the numbers: ",sum)
