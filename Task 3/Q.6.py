#6.Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
x= list(range(1,31))
y = x[:5]+x[-6:]
z= []
for i in y:
   i =i*i
   z.append(i)
print(z)
