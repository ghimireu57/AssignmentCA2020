#3.Create a function that takes a list and returns a new list with unique elements of the first list.
def unique_list (x):
   y=[]
   for a in x:
       if a not in y:
           y.append(a)
   return print(y)

unique_list([1,1,2,2,3,3,4,4,56,8,8,9])