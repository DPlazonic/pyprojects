x = int(input("Enter x value:"))
y = int(input("Enter y value:"))

calculator = input("Choose math operation (+, -, *, /):") 

if calculator == "+":
    print(x + y)
elif calculator == "-":
    print(x - y)
elif calculator == "*":
    print(x * y)
elif calculator == "/":
    print(x / y)
else:
    print("Wrong operation chosen")