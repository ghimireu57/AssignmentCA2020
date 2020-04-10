#10. Write a program in Python to complete the following task:
#Create two different list as in even_list and odd_list
#Ask user to enter the number in the range of 1,50 and make sure if the entered number is even append it to the
# even_list and if the entered number is odd append it to the odd list.
#Keep that in mind you can only add 5 items in each list
#Make sure once you entered the total 5 element calculate the sum of the list and return the maximum out of the list.



Even_list = []
Odd_list = []
while True:
   x = int(input('please enter a value between 0-50'))
   if x in range(51):
       if x % 2 == 0:
           Even_list.append(x)
           if len(Even_list) == 5 and len(Odd_list) >= 5:
               print(Even_list[:5])
               print(sum(Even_list[:5]), ':the sum of 5 Element')
               print(max(Even_list[:5]), ':the maximum of 5 element')
               print(Odd_list[:5])
               print(sum(Odd_list[:5]), ':the sum of 5 Element')
               print(max(Odd_list[:5]), ':the maximum of 5 element')
               break
           elif len(Even_list) > 4:
               print('you can enter only 5 even element')
       else:
           Odd_list.append(x)
           if (len(Odd_list)) == 5 and len(Even_list) >= 5:
               print(Even_list[:5])
               print(sum(Even_list[:5]), ':the sum of 5 Element')
               print(max(Even_list[:5]), ':the maximum of 5 element')
               print(Odd_list[:5])
               print(sum(Odd_list[:5]), ':the sum of 5 Element')
               print(max(Odd_list[:5]), ':the maximum of 5 element')
               break
           elif len(Odd_list) > 4:
               print('you can enter only  5 odd element')
   else:
        print('You have enter a value out of the range')
