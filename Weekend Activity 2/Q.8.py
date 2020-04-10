#8.Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.
def generate_squarenum():
   x = list(range(1, 21))
   z = []
   for i in x:
       i *= i
       z.append(i)
   y = tuple(z)
   return y


print(generate_squarenum())

