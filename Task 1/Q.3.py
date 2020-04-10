#3. Swap two numbers using the third variable as the result name and do the same task without using any third variable.
# Without using third variable
a=int (input('Enter a value for a'))
b =int (input ('Enter a value for b'))
a= a +  b
b = a - b
a = a - b
print (a,b)
print(a)
print(b)

# using third variable
a=input('enter first num')
b=input('enter second num')
print(a)
print(b)
c = a
a = b
b = c
print(a)
print(b)
