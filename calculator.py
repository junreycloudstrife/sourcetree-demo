print('This is a calculator')

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

# print('First num: ' + str(num1))
# print('Second num: ' + str(num2))

oper = input('Enter operator: ')

if (oper == '+'):
    print('Result is equal to :' + str(num1 + num2))
elif (oper == '-'):
    print('Result is equal to :' + str(num1 - num2))
elif (oper == '*'):
    print('Result is equal to :' + str(num1 * num2))
elif (oper == '/'):
    print('Result is equal to :' + str(num1 / num2))
