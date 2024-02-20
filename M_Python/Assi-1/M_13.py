def calculate(x, y, operation):
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        return x / y if y != 0 else "Error: Division by zero"
    else:
        return "Error: Invalid operation"

num1, num2 = float(input("Enter the first number: ")), float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
result = calculate(num1, num2, operation)
print(f"The result is: {result}")
