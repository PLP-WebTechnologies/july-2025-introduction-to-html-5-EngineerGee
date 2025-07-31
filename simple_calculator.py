num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operation = input("Enter operation sign{eg:+ ,- ,/ or *}: ")
if operation == "+":
    result = num1 + num2
    print(f"Result: num1 + num2 = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"Result: num1 - num2 = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"Result: num1 * num2 = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: num1 / num2 = {result}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operation selected.")
