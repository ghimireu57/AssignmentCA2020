#7.Write a program in Python to reverse a string and print only
# the vowel alphabet if exist in the string with their index.
x=(input('please enter a string value'))
y=x[::-1]
b=['a','e','i','o','u']
for i in y:
   if i in b:
       print(i,y.index(i))
