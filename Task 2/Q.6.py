# 6 What is the output of the following code examples?
x=123
for i in x:
    print(i)

#int obj is not iterable(error)

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print('error')

#output: 0,1,2

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        Break

#output: 0,1,2,3,4