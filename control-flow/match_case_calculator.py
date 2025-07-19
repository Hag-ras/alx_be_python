first = int(input('Enter the first number: '))
second = int(input('Enter the second number: '))
operation = input('Choose the operation (+, -, *, /): ')

match operation:
    case '+':
        print('The result is ', first + second)
    case '-':
        print('The result is ', first - second)
    case '*':
        print('The result is ', first * second)
    case '/':
        if second==0:
            print('Cannot divide by zero.')
        else:
            print('The result is ', first / second)
    case _:
        print('Invalid Operation')