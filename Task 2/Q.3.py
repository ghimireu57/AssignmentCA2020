#3.Write a program in Python to implement the given flowchart:

a,b,c=10,20,30
Avg=(a+b+c)/3
if Avg>a and Avg>b and Avg>c:
   print('Avg is higHer than abc')
elif Avg>a and Avg>b:
    print('Avg is higHer than abc')
elif Avg > a and Avg > c:
    print('Avg is higHer than abc')
elif Avg > b and Avg > c:
    print('Avg is higHer than abc')
elif Avg > a:
    print('Avg is higHer than a')
elif Avg > b:
    print('Avg is higHer than b')
elif Avg > c:
    print('Avg is higHer than c')