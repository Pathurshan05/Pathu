def find_max(a,b):
    if(a>b):
            return a
    else:
            return b
num1 = int (input("Enter fist number:"))
num2 = int (input("Enter second number:"))

max1 = find_max(num1 , num2)

print("Maximum of first two: ", max1)