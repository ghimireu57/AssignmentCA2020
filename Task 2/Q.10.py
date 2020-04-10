#10 Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as
'''counter=1
While counter <= 5:
print(“Type in the”, counter, “number”)
		counter=counter+1
#The program asks for five guesses (no matter whether the correct number was guessed or not).
# If the correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
 # After the fifth guess it stops and prints “Game over!”.
                                                          '''
ans = 100
counter = 1
while counter <= 5:
    num = int(input("Guess the lucky number "))
    print('your', counter, "number", num)
    counter = counter + 1

    if num != ans:
        print("Try again.")
    else:
        print("Good guess!")
else:
    print("Game over")
