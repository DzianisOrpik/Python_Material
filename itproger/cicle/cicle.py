num = input("Enter: ")

if int (num) > 0:
    if int (num) >10:
        print ("You entered dig > 10")
        if int (num) >= 50:
            print ("Your dig >= 50")
    else:
       print ("You entered dig > 0 but < 10")
elif int (num) < -10:
    print ("You entered dig < -10")
else:
    print ("You entered dig > 0 but < -10")

name = input()
A = 'Yes' if name != "Test" else 'No'
print ("A")


