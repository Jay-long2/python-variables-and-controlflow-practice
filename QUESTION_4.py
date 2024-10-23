def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operator."

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
operator = input("Enter an operation (+, -, *, /): ")
result = calculate(num1, num2, operator)
print("The result is:", result)