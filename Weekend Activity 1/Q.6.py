#6.Write a program in Python to iterate through the list of numbers in
# the range of 1,100 and print the number which is divisible by 3 and a multiple of 2.

for x in range(0,100):
   if x%2==0 and x%3==0:
       print('the number divisible by 3 and multiple of 2 are:',x)