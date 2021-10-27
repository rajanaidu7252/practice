x = float(input("enter a number:"))
op = input("enter operator:")
y = float(input("enter a number:"))

if op == "+":
    print("addition of ", x, "and", y, "is", x+y)

elif op == "-":
    print("subtraction of ", x, "and", y, "is", x-y)

elif op == "*":
    print("multiplication of ", x, "and", y, "is", x*y)

elif op == "/":
    if y != 0:
        print("division of ", x, "and", y, "is", x/y)
    else:
        print("division of ", x, "and", y, "is:", "infinity")
        print("error: division by zero not possible")
elif op == "**":
    print(x, "to the power", y, "is", x ** y)

else:
    print("invalid inputs")
