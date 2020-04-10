#8.Create a new dictionary by concatenating the following two dictionaries:
#a={1:10,2:20}
#b={3:30,4:40}
#Expected Result: {1:10,2:20,3:30,4:40}
x={1:10, 2:20}
y={3:30, 4:40}
z= {}
for d in (x, y ): z.update(d)
print(z)
