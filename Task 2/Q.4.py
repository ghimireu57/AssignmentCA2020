
# 4 Write a program in Python to break and continue if the following cases occurs:
#If user enters a negative number just break the loop and print “It’s Over”
#If user enters a positive number just continue in the loop and print “Good Going”

x=int(input('Enter a value to get result'))
while x > 0:
   print('Good Going')
   continue
else:
   print("its over")