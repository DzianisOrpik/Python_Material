i = 0
while i < 10:
    print (i)
    i += 2

y = 1000
while y >= 10:
    print (y)
    y /= 2

x = input("Please Enter: ")
while x >= 100:
    print (x)
    x -= 3

for j in 'hello world':
    if j == 'a':
        break
    print (j * 3)
else:
    print ("we do not have")