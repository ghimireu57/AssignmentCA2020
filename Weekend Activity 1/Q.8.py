#8. Write a program in Python to iterate through the string “hello my name is abcde” and
# print the string which has even length of word.
x=('hello my name is abcde')
y=x.split(' ')
z = []
for i in y:
   if len(i)%2 == 0:
       z.append(i)
print('the string with even length of word:', z)
