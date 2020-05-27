print('This is basic calculator with basic operations')
print('1. Enter the first number')
print('2. Enter the second number')
print('3. Enter the operator')

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

oper = input('Enter operator: ')

if (oper == '+'):
    print('Result is equal to :' + str(num1 + num2))
elif (oper == '-'):
    print('Result is equal to :' + str(num1 - num2))
elif (oper == '*'):
    print('Result is equal to :' + str(num1 * num2))
elif (oper == '/'):
    print('Result is equal to :' + str(num1 / num2))
elif (oper == '%'):
    print('Result is equal to :' + str(num1 % num2))
