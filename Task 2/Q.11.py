#11. In the previous question, insert “break” after the “Good guess!” print statement.
# “break” will terminate the while loop so that users do not have to continue guessing after they found the number.
# If the user does not guess the number at all, print “Sorry but that was not very successful”.
ans=100
counter=1
while counter <= 5:
   num = int(input("Guess the lucky number "))
   print('your',counter,"number",num)
   counter = counter + 1
   if num != ans:
       print ("Try again.")
   else:
       print ("Good guess!")
       break
else:
   print("sorry but that was not very successful")
