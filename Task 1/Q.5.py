# 5. Write a program to complete the task given below:
# Ask the user to enter any 2 numbers in between 1-10 and add both of them to another variable call z.
# Use z for adding 30 into it and print the final result by using variable result.

x = int (input("Enter 1st number between 1 to 10: "))
y = int (input("Enter 2nd number between 1 to 10: "))
z = x+y
if(0 < x <= 10 and 0 < y <= 10):
    total = z+30
    print("Grand Total(z+30)= "+str(total))
else:
    print("Enter the proper number between 1 to 10.")