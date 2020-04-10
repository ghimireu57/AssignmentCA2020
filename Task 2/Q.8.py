#8 Write a program that accepts a string as an input from user and calculate the number of digits and letters.
#.Expected output: consul12
#Letters 6
#Digits 2
x = input("Please enter you desired value:")
c1 = 0
c2 = 0
for i in x:
 if i.isdigit():
   c1 += 1
 if i.isalpha():
   c2 += 1
print("Letters:",c2)
print("Digits:", c1)