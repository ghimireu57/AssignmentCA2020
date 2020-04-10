#2 Write a program in Python to perform the following operator based task:
#Ask user to choose the following option first:
#If User Enter 1 - Addition
#If User Enter 2 - Subtraction
#If User Enter 3 - Division
#If USer Enter 4 - Multiplication
#If User Enter 5 - Average

#Ask user to enter the 2 numbers in a variable for first and second for the first 4 options mentioned above.
#Ask user to enter two more numbers as first1 and second2 for calculating the average as soon as user choose an option
# 5.At the end if the answer of any operation is Negative print a statement saying “zsa”
#NOTE: At a time user can perform one action at a time.
x = int(input('Please enter the Value \n Enter 1 - Addition \n Enter 2 - Subtraction \n Enter 3 - Division\n Enter 4 - Multiplication \n Enter 5 - Average'))

if x not in range (1,6):
   print ('You enter a wrong number')
elif x in range (1,6):
   y = int(input('please enter the first number to perform calculation'))
   z = int(input('Please enter the Second number to perform calculation'))
   if x in range(1,5):
       if x == 1:
           print ('Addition of two num:', y+z)
           if y+z<0:
               print('zsa')
       if  x == 2:
           print('subtraction of two num:',y-z)
           if y-z<0:
               print('zsa')
               if x == 3:
                   print('Division of two num:', y / z)
                   if y / z < 0:
                       print('zsa')
               if x == 4:
                   print('Multiplication of two num:', y * z)
                   if y * z < 0:
                       print('zsa')
               if x == 5:
                   a = int('Enter the First Number for average')
                   b = int('Enter the Second Number for Average')
                   print('Average value of 4 Num:', (y + z + a + b) / 4)
                   if (y + z + a + b) / 4:
                       print('zsa')