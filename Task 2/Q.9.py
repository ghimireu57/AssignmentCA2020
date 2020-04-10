# 9 Read the two parts of the question below:
#Write a program such that it asks users to “guess the lucky number”.
# If the correct number is guessed the program stops, otherwise it continues forever.
#Modify the program so that it asks users whether they want to guess again each time.
# Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question
# they want to continue guessing. The program stops if the user guesses the correct number or answers “no”.
# ( The program continues as long as a user has not answered “no” and has not guessed the correct number)

num=int(input('Enter the Your Lucky Number'))
ans=999
while num!=ans:
   x=input("DO you want to play again?\n:Y/N")
   if x == "Y":
       y=int(input('Enter you Lucky Number Again'))
       if y== ans:
           print("congratulation you have got lucky number")
           break
       else:
           continue
   if x=="N":
        print("you are out of the game")
        break
else:
   print("congratulation you have got lucky number")