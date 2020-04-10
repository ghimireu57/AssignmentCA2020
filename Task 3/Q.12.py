
# Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

x=(1,2,3,4,5,6,7,8,9,10)
y=[]
for i in x:
    if i %2 == 0:
        y.append(i)
z = tuple(y)
print(z)
print(type(z))

#or
x=(1,2,3,4,5,6,7,8,9,10)
y=list(x)
for i in y:
    if i %2 != 0:
        y.remove(i)
z = tuple(y)
print(type(z))
print(z)