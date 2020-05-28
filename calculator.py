print('This is a basic calculator')
print('Enter the first number')
print('Enter the second number')
print('Enter the operator')

def operations(operator):
    switcher = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2,
        '%': num1 % num2
    }
    return switcher.get(operator, "Invalid operator")

num1 = int(input("First number: "))
num2 = int(input("Second number: "))
oper = input("Enter operator: ")
result = operations(oper)
print("Result is equal to " + str(result))

